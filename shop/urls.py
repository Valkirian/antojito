from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Auth
    path('singup', views.singup, name="singup"),
    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),
    path('accounts/login/', views.login, name="redirectToLogin"),
    # Pages
    path('', views.home, name="home"),
    path('home', views.ppage, name="ppage"),
    path('payment', views.payment, name="payment"),
]
