from django import forms
from product.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter product name'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rate': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        labels = {
            'name': 'Product Name',
            'price': 'Price',
            'image': 'Image',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'product', 'created_at', 'updated_at']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your review here'
                }
            ),
        }
        labels = {
            'text': 'Review Text',
        }
