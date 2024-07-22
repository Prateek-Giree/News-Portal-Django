from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'a_news/home.html')


def news(request):
    return render(request, 'a_news/capital.html')


def login(reqest):
    return render(reqest, 'form.html')
