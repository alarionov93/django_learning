from django.conf.urls import patterns, include, url
from . import views
import userprofile

urlpatterns = patterns('',
    url(r'^profile/$', userprofile.views.user_profile, name='profile'),
    # TODO: find solution instead of this shit!! hope this is temporary.
    url(r'^login/$', userprofile.views.redirect_to_login, name='redirect_to_login'),
)
