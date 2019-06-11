from django.shortcuts import render
from .queryBoolean import *
from .readDB import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def description_search(request):
    return render(request,'result.html')

def ingredient_search(request):
    query = request.GET['query2']
    candidate = FindN(query)
    
    NAdata_name = NA_Ingredient_nameonly(candidate, db)
    return render(request,'result.html',{'NAdata_name':NAdata_name})