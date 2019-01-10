from django.urls import path
from . import views # Importing views.py file from the current directory

app_name = 'article'

urlpatterns = [
    path('',views.articleList, name = 'arlist'),
    # Whatever we enter after /article in the url will be captured in the slug field and this is
    # passed on to details function.
    path('new/',views.create, name = 'create'),
    path('about/',views.aboutDesigner, name = 'about'),
    path('contact/',views.contactDesigner, name = 'contact'),
    path('<str:pagename>/',views.details, name = 'urlname'),
]
