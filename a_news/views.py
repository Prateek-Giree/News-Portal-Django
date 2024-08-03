from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import News, User
from django.contrib.auth.hashers import make_password

# Create your views here.


def home(request):
    page = 'home'
    categories = ['capital', 'nation', 'politics', 'global',
                  'stock', 'sports', 'science_tech', 'weather']
    news_by_category = {category: News.objects.filter(
        category=category) for category in categories}

    recent_news = News.objects.order_by('-date')[:5]
    context = {
        'news_by_category': news_by_category,
        'recent_news': recent_news,
        'page': page,
    }
    return render(request, 'a_news/home.html', context)


def news(request, pk):
    all_news = News.objects.all()
    news = News.objects.get(pk=pk)
    context = {
        'news': news,
        # 'news_category': news_category,
        'all_news': all_news
    }
    return render(request, 'a_news/news.html', context)


def newsByCategory(request, category):
    news = News.objects.filter(category=category)
    context = {
        'news': news,
        'category':  category.capitalize(),
    }
    return render(request, 'a_news/category.html', context)

def loginView(request):

    # if user is already logged in then redirect to home. Prevent relogin
    if request.user.is_authenticated:
        return redirect("postnews")

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)  # create session
                return redirect("postnews")
            else:
                messages.error(request, "Username or password does not match")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
    
    #to render login form
    page='RenderLogin'
    context = {
        'page':page,
    }
    return render(request, 'form.html', context)


def register(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password != cpassword:
            messages.error(request, "Password do not match.")
        
        else:
            # Check if the email is already registered
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
            else:
                # Create a new user with the form information
                user = User(
                    name=name,
                    email=email,
                    password=make_password(password),
                )
                user.save()
                messages.success(request, "User registered successfully.")
                return redirect("login")

    return render(request, 'form.html')

@login_required(login_url='login')
def postNews(request):
    return render(request,'a_news/postnews.html')



