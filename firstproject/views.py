# from django.http import HttpResponse this is one option for the request parameter
from django.shortcuts import render # this is the second option for the request parameter

def homepage(request):
    # return HttpResponse("Welcome to the homepage!") use this with the from django.http import HttpResponse
    return render(request, 'home.html') #this is the second option for the request parameter

def about(request):
    # return HttpResponse("This is the about page.") use this with the from django.http import HttpResponse
    return render(request, 'about.html') #this is the second option for the request parameter