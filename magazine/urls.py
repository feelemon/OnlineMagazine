from django.conf.urls import include, url
from . import views
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
import social.apps.django_app.urls
import paypal.standard.ipn.urls

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),

    url(r'^accounts/logout/$', logout, {'next_page': 'post_list'}, name='logout'),
    url(r'^accounts/loginok/$', login, {'template_name': 'magazine/login.html'}, name='login'),
    url(r'^locus/$', views.locus, name='locus'),
    url(r'^backet/', views.backet, name='backet'),
    # url (r'^post/(?P<pk>[0-9]+)/$'

    #vk
    url(r'^accounts/login/$', views.home, name='home'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),
    url('', include(social.apps.django_app.urls, namespace='social')),

    #Paypal
    url(r'^payment/cart/$', views.paypal_pay, name='cart'),
    url(r'^payment/success/$', views.paypal_success, name='success'),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
]
