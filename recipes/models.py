from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    source_url = models.URLField()
    servings = models.IntegerField()
    prep_time = models.IntegerField()  # in minutes
    calories_per_serving = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)  # "2 cups", "1 tbsp", etc.
    
    def __str__(self):
        return f"{self.amount} {self.ingredient.name}"