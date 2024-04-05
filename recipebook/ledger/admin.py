from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ['ingredient', 'quantity', 'recipe']
    search_fields = ['ingredient', 'quantity', 'recipe']
    list_filter = ['recipe']

    fieldsets = [
        ('Details', {
            'fields' : [
                ('ingredient', 'quantity', 'recipe')
            ]
        })
    ]

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ['recipe_image', 'description', 'recipe']
    search_fields = ['description', 'recipe']
    list_filter = ['recipe']

    fieldsets = [
        ('Details', {
            'fields' : [
                ('recipe_image', 'description', 'recipe')
            ]
        })
    ]
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
