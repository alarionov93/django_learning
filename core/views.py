import json
from django.shortcuts import render, redirect, render_to_response
from django.core import serializers
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
from core.models import Category, Product, Farmer
from django.utils import timezone
import datetime


def index(request):
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})


def category_products(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        products = category.product_set.all()
    except Category.DoesNotExists:
        raise Http404("Category does not exists.")
    return render(request, 'category_products.html', {'products': products})


def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExists:
        raise Http404("Product does not exists.")
    return render(request, 'product.html', {'product': product})


def farmers(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmers.html', {'farmers': farmers})


def farmer(request, farmer_id):
    try:
        farmer = Farmer.objects.get(pk=farmer_id)
        his_categories = Category.objects.filter(farmer__id=farmer.id)
        his_products = Product.objects.filter(farmer__id=farmer.id)
        ctx = {
            'farmer': farmer,
            'categories': his_categories,
            'products': his_products,
        }
    except Farmer.DoesNotExists:
        raise Http404("Farmer does not exists.")
    return render(request, 'farmer.html', ctx)


# account views here:

def login(request):
    ctx = {}
    ctx.update(csrf(request))
    return render_to_response('login.html', ctx)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/core/')
    else:
        return HttpResponseRedirect('/core/accounts/invalid/')


def logged_in(request):
    ctx = {
        'full_name': request.user.username,
        # 'user': request.user,
    }
    return render_to_response('logged_in.html', ctx)


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/core/')
# def books_year(request, year):
    # year = int(year)
    # date = datetime.date(year, 11, 1)
    # books = Book.objects.filter(date__range=(date, date.today()))
    # return HttpResponse(serializers.serialize('json', books))


# def books(request):
#     books = Book.objects.all()
#     return render(request, 'books.html', {'books': books})
#
#
# def book(request, book_id, year=timezone.now().year):
#     try:
#         book = Book.objects.get(pk=book_id)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#     return render(request, 'book.html', {'book': book})
#
#
# def authors(request):
#     author_list = Author.objects.all()
#     for a in author_list:
#         his_books = Book.objects.filter(author__id=a.id)
#         a.count = len(his_books)
#
#     ctx = {
#         'authors': author_list
#     }
#     return render(request, "authors.html", ctx)
#
#
# def author(request, author_id):
#     try:
#         current_author = Author.objects.get(pk=author_id)
#         books = Book.objects.filter(author__id=current_author.id)
#     except Author.DoesNotExist:
#         raise Http404("Author does not exist")
#
#     ctx = {
#         'books': books,
#         'author': current_author
#     }
#     # print(ctx)
#
#     return render(request, "author.html", ctx)
#
#
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
