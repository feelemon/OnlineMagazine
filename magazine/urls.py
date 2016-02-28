from django.conf.urls import include, url
from . import views
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    # url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    # url(r'^$', views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/logout/$', logout, {'next_page': 'post_list'}, name='logout'),
    url(r'^accounts/login/$', login, {'template_name': 'magazine/login.html'}, name='login'),
    url(r'^locus/$', views.locus, name='locus'),
]
