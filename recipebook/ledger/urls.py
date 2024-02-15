from django.urls import path
from .views import recipe_list, recipe1, recipe2

urlpatterns = [
    path('recipe/list/', recipe_list, name='list'),
    path('recipe/1/', recipe1, name='1'),
    path('recipe/2/', recipe2, name='2'),
]

app_name = "ledger"