from django.shortcuts import render
from .models import Bicycle
from cart.forms import CartAddProductForm
# Create your views here.

def index(request):
	bicycles=Bicycle.objects.all()
	cart_product_form = CartAddProductForm()

	return render(request, "index.html", {"bicycles":bicycles, "cart_product_form":cart_product_form})