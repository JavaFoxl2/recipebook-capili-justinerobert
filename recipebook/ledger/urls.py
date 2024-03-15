from django.urls import path
from django.contrib import admin
from .views import RecipeListView, RecipeDetailView, RecipeDetailView_LoggedIn

urlpatterns = [
    path('recipes/list',RecipeListView.as_view(), name="recipes"),
    path('recipe/<int:pk>', RecipeDetailView_LoggedIn.as_view(), name='recipe_detail')
]

app_name = "ledger"