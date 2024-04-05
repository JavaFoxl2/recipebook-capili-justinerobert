from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


def index(request):
    return HttpResponse('landing page')


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = '/recipes/list'


class AddRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'

    def get_success_url(self):
        return reverse_lazy('ledger:recipes_list')


class AddRecipeImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_add_image.html'
    
    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={ 'pk': self.object.recipe.pk })

        