from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def description_search(request):
    return render(request,'result.html')

def ingredient_search(request):
    return render(request,'result.html')