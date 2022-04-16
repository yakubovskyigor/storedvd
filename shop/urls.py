from django.urls import path, re_path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    re_path('blog', views.blog, name='blog'),
    re_path('single', views.single, name='single'),
    # re_path(r'single/(?P<pk>\d+)$', views.SingleDetailView.as_view(), name='single'),

]