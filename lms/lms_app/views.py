from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.decorators.cache import never_cache
from django.db.models import Sum


def index(request):
    total_sold = Book.objects.filter(status='sold').aggregate(total_price=Sum('price')).get('total_price') or 0
    total_rented = Book.objects.filter(status='rented').aggregate(total_rental=Sum('total_rental')).get('total_rental') or 0
    total_sum=total_sold+total_rented


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
        'total_price': Book.objects.filter(status='sold').aggregate(total_price=models.Sum('price'))['total_price'],
        'total_rental': Book.objects.filter(status='rented').aggregate(total_rental=models.Sum('total_rental'))['total_rental'],
        'total_sold': total_sold,
        'total_rented': total_rented,
        'total_sum': total_sum,
    }
    
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None

    # Handle search functionality
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    # Handle category form submission (for POST requests)
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('books')  # Redirect after saving the form

    # Define the context dictionary (for both GET and POST requests)
    context = {
        'books': search,  # Books filtered by search (if any)
        'categories': Category.objects.all(),  # All categories
        'category_form': CategoryForm(),  # Empty form for GET requests
    }

    # Render the template with the context
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
