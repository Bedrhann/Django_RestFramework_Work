

from django.urls import path
from . import views

urlpatterns = [
    path('products',views.Product),
    path('about-us',views.AboutUs),
    path('contact',views.Contact)

]
