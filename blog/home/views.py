from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def Home_page(request):
#     return render(request,'home.html',{})

def Home_page(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'Barış'
        }
    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'home.html', context)