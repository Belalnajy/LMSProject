from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.decorators.cache import never_cache

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)
        if add_book.is_valid():
            add_book.save()
            return redirect('index')
        if category_form.is_valid():
            category_form.save()
            return redirect('index')
    context= {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'category_form': CategoryForm(),
        'count_book': Book.objects.filter(active=True).count(),
        'sold_book': Book.objects.filter(status='sold').count(),
        'available_book': Book.objects.filter(status='available').count(),
        'rented_book': Book.objects.filter(status='rented').count(),
    }

    return render(request, 'pages/index.html', context)
def books(request):
    context= {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'pages/books.html', context)



def update(request, id):
    # book_id = Book.objects.get(id=id)
    book_id = get_object_or_404(Book, id=id)  # Safer than Book.objects.get()

    if request.method == 'POST':
        update_book = BookForm(request.POST, request.FILES, instance=book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect('/')
    else:
        update_book = BookForm(instance=book_id)  

    context = {
        'form': update_book,
    }
    return render(request, 'pages/update.html', context)



@never_cache
def delete(request, id):
    book_id=get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')
# Create your views here.
