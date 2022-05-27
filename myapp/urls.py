from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('next', next, name='next'),
    path('next_page', next_page, name='next_page'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('post/<str:pk>/', post, name='post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)