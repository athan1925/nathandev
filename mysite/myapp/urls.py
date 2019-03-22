from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
]