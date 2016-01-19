from django.conf.urls import url
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^books/$', views.books, name='books'),

    url(r'^books/(?P<book_id>[0-9]+)/$', views.book, name='book'),

    url(r'^books_year/(?P<year>[0-9]+)/$', views.books_year, name='books_year'),

    # url(r'^books_year/(?P<year>[0-9]+)/(?P<book_id>[0-9]+)/$', views.book, name='book_year'),

    url(r'^authors/$', views.authors, name='authors'),

    url(r'^authors/(?P<author_id>[0-9]+)/$', views.author, name='author'),

    #
    # url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]