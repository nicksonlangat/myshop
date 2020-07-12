from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Bicycle
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, bicycle_id):
	cart = Cart(request)
	bicycle = get_object_or_404(Bicycle, id=bicycle_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(bicycle=bicycle,
			quantity=cd['quantity'],
			override_quantity=cd['override'])
	return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, bicycle_id):
	cart = Cart(request)
	bicycle = get_object_or_404(Bicycle, id=bicycle_id)
	cart.remove(bicycle)

	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart': cart})
