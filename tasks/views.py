from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home_page(request):
    return render(request, "home.html")
