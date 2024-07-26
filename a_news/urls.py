from django.urls import path
from .views import home, news, loginView, register, newsByCategory

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>', news, name='news'),
    path('login/', loginView, name='login'),
    path('register/', register, name='register'),
    path('newsByCategory/<str:category>',
         newsByCategory, name='newsByCategory'),
]
