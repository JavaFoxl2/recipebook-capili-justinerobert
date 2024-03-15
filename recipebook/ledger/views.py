from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RecipeListView (ListView):
    model = Recipe
    template_name = 'recipe.html'

class RecipeDetailView (DetailView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView_LoggedIn (LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes_list.html'
