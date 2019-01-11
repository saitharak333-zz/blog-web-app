from django.urls import path
from . import views # Importing views.py file from the current directory

app_name = 'users'

urlpatterns = [
    path('signup/',views.signup_func, name = 'usrsignup'),
    path('signin/',views.signin_func, name = 'letssignin'),
    path('signin/signup',views.signup_func, name = 'ursssignup'),
    path('signout/', views.signout_func, name = 'usrsignout'),
]
