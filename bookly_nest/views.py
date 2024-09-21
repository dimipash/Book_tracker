from django.shortcuts import render
from .models import Book, Genre

def index(request):
    books = Book.objects.all()    
    context = {
        'books': books,
    }
    return render(request, 'bookly_nest/index.html', context=context)

def genres(request):
    genres = Genre.objects.all()
    context = {
        "genres": genres,
    }
    return render(request, "bookly_nest/genres.html", context=context)

def genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    books = genre.book_set.order_by('-date_added')
    context = {
        "genre": genre,
        "books": books,
    }
    return render(request, "bookly_nest/genre.html", context=context)