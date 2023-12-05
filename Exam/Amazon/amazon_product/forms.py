from django import forms
from django.contrib.auth.models import User

from .models import Product

type_product_choices = (
    ("Fashion", "Fashion"),
    ("Food", "Food"),
    ("Dress", "Dress"),
    ("Sneaker", "Sneaker"),
    ("Perfume", "Perfume"),
    ("Technique", "Technique"),
    ("Toys", "Toys"),
    ("Others", "Others"),
)


class Product_Forms(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Product name",
                            help_text="How your product will be called")
    genre = forms.CharField(max_length=255, label="Type", help_text="Enter main type of your product",
                            widget=forms.Select(choices=type_product_choices))
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Price",
                               help_text="Please enter price")
    image = forms.ImageField(required=False, label="Product photo",
                             help_text="Please upload product photo")
    description = forms.CharField(max_length=255, label="Description", help_text="Please enter description",
                                  widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))

    class Meta:
        model = Product
        fields = [ 'image', 'title', 'genre', 'price', 'description']