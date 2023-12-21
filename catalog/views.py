from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, 'catalog/contacts.html')
