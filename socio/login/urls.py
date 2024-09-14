from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration/',views.registration,name='registration'),
    path('home/',views.home,name='home'),
    path('verify/',views.verify,name='verify'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/<int:id>',views.pro1,name='pro1'),
    path('createRequest/<int:id>',views.cre,name='cre'),
    path('Request/',views.Request,name='Request/'),
]
