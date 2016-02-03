from django.conf.urls import url
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
    # working urls

    ###################
    # categories routes

    # /core/
    url(r'^$', views.index, name='index'),

    # /core/categories/
    url(r'^categories/$', views.index, name='index_cat'), # double route

    # /core/category/3/products/
    url(r'^category/(?P<category_id>[0-9]+)/products/$', views.category_products, name='category_products'),

    #################
    # products routes

    # TODO: is /core/products/ needed in app?
    # /core/product/1/
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),

    ################
    # farmers routes

    # /core/farmers/
    url(r'^farmers/$', views.farmers, name='farmers'),

    # /core/farmer/2/
    url(r'^farmer/(?P<farmer_id>[0-9]+)/$', views.farmer, name='farmer'),


    #
    # url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]