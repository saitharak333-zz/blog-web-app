from django.urls import path
from . import views # Importing views.py file from the current directory

app_name = 'users'

urlpatterns = [
    path('signup/',views.signup_func, name = 'signup'),
    path('login/', views.signup_func, name = 'login'),
    path('usrlogin/',views.login_func, name = 'userlogin'),
    path('logout/', views.logout_func, name = 'logout'),
]
