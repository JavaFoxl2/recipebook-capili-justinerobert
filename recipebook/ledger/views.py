from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
 
def index(request):
    return HttpResponse("Recipe Book")

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe.html"
    