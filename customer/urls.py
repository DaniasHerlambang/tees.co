from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.CustomerView.as_view(), name='customer'),
    path('api/<str:pk>', views.CustomerView.as_view(), name='profil'),
]
