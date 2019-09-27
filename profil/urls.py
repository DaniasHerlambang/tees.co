from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ProfilView.as_view(), name='profil'),
    path('api/<str:pk>', views.ProfilView.as_view(), name='profil'),

]
