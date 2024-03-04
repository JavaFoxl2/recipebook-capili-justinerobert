from django.contrib import admin

from .models import *

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    fields = ['ingredient', 'quantity', 'recipe']

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    search_fields = ('name',)
    list_display = ('name',)

    inlines = [RecipeIngredientInLine]

admin.site.register(Recipe, RecipeAdmin)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name',)
    list_display = ('name',)

    inlines = [RecipeIngredientInLine]


admin.site.register(Ingredient, IngredientAdmin)

# Register your models here.
