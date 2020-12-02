from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    html = "<h1>Welcome to the Tomb of Horror</h1>"
    return HttpResponse(html)