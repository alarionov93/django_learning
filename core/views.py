from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from core.models import Book, Author

# Create your views here.


def index(request):
    return HttpResponse("Hello world!")


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book.html', {'book': book})


def authors(request):
    author_list = Author.objects.all()
    for a in author_list:
        his_books = Book.objects.filter(author__id=a.id)
        a.count = len(his_books)

    ctx = {
        'authors': author_list
    }
    return render(request, "authors.html", ctx)


def author(request, author_id):
    try:
        current_author = Author.objects.get(pk=author_id)
        books = Book.objects.filter(author__id=current_author.id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    ctx = {
        'books': books,
        'author': current_author
    }
    print(ctx)

    return render(request, "author.html", ctx)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
