from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"trypage.html")


def pop(request):
    return HttpResponse("hellopop")




def lekhr(request):
    return HttpResponse("hello lekher")
def nom(request,name):
    return render(request,"otherpage.html",{
        "name": name.capitalize()
    })