from django.urls import path

from .views import index, RecipeListView, RecipeDetailView, AddRecipeView, AddRecipeImageView


urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', AddRecipeView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', AddRecipeImageView.as_view(), name='recipe_add_image')
]

app_name = "ledger"