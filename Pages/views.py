from django.http import HttpResponse
from django.shortcuts import render

contact_info = ["05433345","ahmet sonmez","çanakkale"]

def Product (request):
    return HttpResponse("ÜRÜN SAYFASI")

def AboutUs (request):
    return HttpResponse("HAKKIMIZDA")

def Contact (request):
    data = {
        "bilgiler": contact_info
    }
    return render(request,"index.html",data)
