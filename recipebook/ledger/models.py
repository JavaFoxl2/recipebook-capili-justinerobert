from django.db import models
from django.urls import reverse
from accounts.models import Profile

# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    author = models.ForeignKey (
        Profile, 
        on_delete=models.PROTECT, 
        related_name = "authors", 
        null=True
    )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=str(self.pk))

class Ingredient (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RecipeIngredient (models.Model):
    quantity = models.CharField(max_length=100)

    recipe = models.ForeignKey (
        Recipe, 
        on_delete=models.CASCADE, 
        related_name = 'ingredients'
    )
    ingredient = models.ForeignKey (
        Ingredient, null=True, 
        on_delete=models.CASCADE, 
        related_name = 'recipes'
    )