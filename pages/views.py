from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1>") # String of HTML code


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")