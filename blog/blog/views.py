from django.http import HttpResponse
# To send the response back to the user.
from django.shortcuts import render
# To send the html templates back to user.

def homepage(request):
    # return HttpResponse('Home Page') #Sending text as an response
    return render(request, 'home.html')
def about(request):
    # return HttpResponse('About') #Sending text as an response
    return render(request, 'about.html')
