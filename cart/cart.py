from decimal import Decimal
from django.conf import settings
from core.models import Bicycle

class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}

		self.cart = cart
	def add(self, bicycle, quantity=1, override_quantity=False):
		bicycle_id = str(bicycle.id)
		if bicycle_id not in self.cart:
			self.cart[bicycle_id] = {'quantity': 0,'price': str(bicycle.price)}
		if override_quantity:
			self.cart[bicycle_id]['quantity'] = quantity
		else:
			self.cart[bicycle_id]['quantity'] += quantity
		self.save()
	def save(self):
		self.session.modified = True

	def remove(self, bicycle):
		bicycle_id = str(bicycle.id)
		if bicycle_id in self.cart:
			del self.cart[bicycle_id]
			self.save()
			
	def __iter__(self):
		bicycle_ids = self.cart.keys()
		bicycles = Bicycle.objects.filter(id__in=bicycle_ids)
		cart = self.cart.copy()

		for bicycle in bicycles:
			cart[str(bicycle.id)]['bicycle'] = bicycle

		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item
	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()





 