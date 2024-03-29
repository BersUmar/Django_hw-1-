from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView, PasswordContextMixin
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import UpdateView, CreateView, FormView, TemplateView
from pip._internal.utils._jaraco_text import _
from config import settings
from users.forms import UserUpdateForm, UserRegisterForm
from users.models import User
from users.utils import generation_password


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def form_valid(self, form):
        """ Дружественное письмо на почту пользователя, после регистрации """
        new_user = form.save()
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))
        new_token = token_generator.make_token(new_user)
        activation_url = reverse_lazy('users:verify_email', kwargs={'uidb64': uid, 'token': new_token})
        send_mail(
            subject='Активация учетной записи',
            message=f'Пройдите по ссылке, чтобы закончить регистрацию: http://127.0.0.1:8000/{ activation_url }',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False
        )
        return redirect('users:confirm_email')


class UserPasswordResetView(PasswordContextMixin, FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy("users:password_reset_done")
    title = _("Password reset")
    template_name = 'users/password_reset_form.html'

    def form_valid(self, form):
        """ Дружественное письмо на почту пользователя, после регистрации """
        user_email: str = self.request.POST.get('email')
        new_password: str = generation_password()
        user_object: object = User.objects.get(email=user_email)
        send_mail(
            subject='Восстановление пароля',
            message=f'Вы запросили новый пароль для {user_email}.\nВаш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email]
        )
        user_object.set_password(new_password)
        user_object.save()
        return super().form_valid(form)


class UserPasswordResetDoneView(PasswordResetDoneView):
    PasswordResetDoneView.template_name = 'users/password_reset_done.html'


class UserActivate(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            send_mail(
                subject='Успешная активация',
                message=f'Вы успешно активировали учетную запись!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return redirect('users:user_activate')
        return redirect('users:invalid_user_activate')


    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user


class InvalidUserActivate(TemplateView):
    template_name = 'users/invalid_user_activate.html'