from django import forms
from .models import Book, Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'author_image', 'book_image', 'pages', 'price', 'retal_price_day', 'retal_period','total_rental', 'status', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'author_image': forms.FileInput(attrs={'class': 'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class': 'form-control','id':'retal_price_day'}),
            'retal_period': forms.NumberInput(attrs={'class': 'form-control','id':'retal_period'}),
            'total_rental': forms.NumberInput(attrs={'class': 'form-control','id':'total_rental','readonly':'readonly'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }