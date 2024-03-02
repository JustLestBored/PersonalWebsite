from django.urls import path
from . import views
app_name='base'

urlpatterns = [
    path ('', views.home, name='home'),
    path ('About', views.abouts, name='about'),
    path ('Resume', views.resume, name='resume'),
    path ('Contact', views.contact, name='contact'),
    path ('Gallery', views.gallery, name='gallery'),
]