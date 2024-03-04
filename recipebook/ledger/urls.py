from django.urls import path
from django.contrib import admin
from .views import index, RecipeDetailView, RecipeListView

urlpatterns = [
    path('', index, name="index"),
    path('recipes/list',RecipeListView.as_view(), name="recipes_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_<int:pk>')
]

app_name = "ledger"