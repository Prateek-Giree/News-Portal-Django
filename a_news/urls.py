from django.urls import path
from .views import home, news, login

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>', news, name='news'),
    path('login/', login, name='login'),
]
