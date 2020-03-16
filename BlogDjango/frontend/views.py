from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html') #going to create urls.py in frontend app folder