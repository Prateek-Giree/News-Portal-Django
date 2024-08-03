from django.urls import path
from .views import home, news, loginView, register, newsByCategory, postNews

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>', news, name='news'),
    path('login/', loginView, name='login'),
    path('register/', register, name='register'),
    path('newsByCategory/<str:category>',
         newsByCategory, name='newsByCategory'),
    path('postnews/', postNews, name='postnews'),
]
