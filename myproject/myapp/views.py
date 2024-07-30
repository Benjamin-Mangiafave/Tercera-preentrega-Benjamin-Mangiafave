from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm, SearchForm

def index(request):
    return render(request, 'index.html')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublisherForm()
    return render(request, 'add_publisher.html', {'form': form})

def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)  # Example search in Book model
    return render(request, 'search.html', {'form': form, 'results': results})

