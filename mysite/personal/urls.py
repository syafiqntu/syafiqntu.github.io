from django.urls import path, include
from . import views #new


urlpatterns = [
    path('', views.index, name='index' ),
    path('contact/', views.contact, name='contact'),
]
