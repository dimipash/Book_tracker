from django.shortcuts import render
from .models import Book, Genre
from .forms import GenreForm, BookForm
from django.shortcuts import redirect

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

def new_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('bookly_nest:genres')
    else:
        form = GenreForm()

    context = {
        "form": form,
    }
    
    return render(request, "bookly_nest/new_genre.html", context=context)

def new_book(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.genre = genre
            book.save()
            return redirect('bookly_nest:genre', genre_id=genre_id)
    else:
        form = BookForm()

    context = {
        "form": form,
        "genre": genre,
    }
    
    return render(request, "bookly_nest/new_book.html", context=context)