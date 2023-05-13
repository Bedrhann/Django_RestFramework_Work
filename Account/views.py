from django.http import HttpResponse
from django.shortcuts import render




def MyInformation (request):
    return HttpResponse("hesap sayfana hoşgeldin")

def Addresses (request):
    return HttpResponse("Adreslerini değiştirme sayfasi")
