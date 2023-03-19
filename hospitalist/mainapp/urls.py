from django.urls import path
from . import views

urlpatterns = [
    path('hospital/create/', views.hospital_detail),
    path('hospital/get/', views.get_hospital_detail),
    path('hospital/all/', views.getAll_hospital_detail),
    path('hospital/edit/<int:pk>/', views.edit_hospital_detail),
]
