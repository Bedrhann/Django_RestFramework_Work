
from django.urls import path
from . import views

urlpatterns = [
    path('',views.MyInformation),
    path('my-information',views.MyInformation),
    path('addresses',views.Addresses)
]
