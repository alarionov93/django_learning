# from core import admin
from django.conf.urls import url, include, patterns
from . import views
# from django.http import HttpResponseRedirect

urlpatterns = patterns('',
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

    ################
    # account routes
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/logged_in/$', views.logged_in, name='logged_in'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),

)