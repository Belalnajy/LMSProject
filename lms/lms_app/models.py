from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    status_book = (
        ('available', 'available'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    author_image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    book_image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    pages = models.IntegerField( null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField( null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100,choices= status_book , null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.title
