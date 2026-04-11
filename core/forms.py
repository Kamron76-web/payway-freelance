from django import forms
from .models import Product, SellerRequest

class ProductForm(forms.ModelForm):
class Meta:
model = Product
fields = ['title', 'description', 'price', 'image']

class SellerRequestForm(forms.ModelForm):
class Meta:
model = SellerRequest
fields = ['passport_image', 'face_image']
