import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def search_recipes_api(ingredients, max_results=10):
    """
    Search for recipes using Edamam Recipe Search API v2
    """
    try:
        # Correct API endpoint for Recipe Search API v2
        url = "https://api.edamam.com/api/recipes/v2"
        
        # Required headers
        headers = {
            'Edamam-Account-User': settings.EDAMAM_APP_ID,  # Use app_id as userID
            'Accept': 'application/json'
        }
        
        # API parameters for v2
        params = {
            'type': 'public',
            'q': ingredients,
            'app_id': settings.EDAMAM_APP_ID,
            'app_key': settings.EDAMAM_APP_KEY,
            'from': 0,
            'to': max_results,
        }
        
        # Make API request with headers
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract recipe information
        recipes = []
        for hit in data.get('hits', []):
            recipe = hit.get('recipe', {})
            
            # Extract ingredients list
            ingredients_list = []
            for ingredient in recipe.get('ingredientLines', []):
                ingredients_list.append(ingredient)
            
            # Extract nutrition info safely
            nutrition = recipe.get('totalNutrients', {})
            calories = nutrition.get('ENERC_KCAL', {}).get('quantity', 0) if nutrition.get('ENERC_KCAL') else 0
            
            # Get servings, default to 1 if not available
            servings = recipe.get('yield', 1) or 1
            
            recipe_data = {
                'title': recipe.get('label', 'Unknown Recipe'),
                'image_url': recipe.get('image', ''),
                'source_url': recipe.get('url', ''),
                'servings': servings,
                'prep_time': recipe.get('totalTime', 0) or 30,
                'calories_per_serving': int(calories / servings) if calories else 0,
                'ingredients': ingredients_list,
                'cuisine_type': recipe.get('cuisineType', ['Unknown'])[0] if recipe.get('cuisineType') else 'Unknown',
                'meal_type': recipe.get('mealType', ['Unknown'])[0] if recipe.get('mealType') else 'Unknown',
                'diet_labels': recipe.get('dietLabels', []),
                'health_labels': recipe.get('healthLabels', []),
            }
            
            recipes.append(recipe_data)
        
        return {
            'success': True,
            'recipes': recipes,
            'total_results': len(recipes)
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        return {
            'success': False,
            'error': f'Failed to fetch recipes. Please check your internet connection and try again.',
            'recipes': []
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            'success': False,
            'error': f'An unexpected error occurred: {str(e)}',
            'recipes': []
        }

def get_mock_recipes(ingredients):
    """Mock data for testing when API is not available"""
    mock_recipes = [
        {
            'title': f'Delicious {ingredients} Recipe',
            'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=300&h=200&fit=crop',
            'source_url': 'https://example.com/recipe1',
            'servings': 4,
            'prep_time': 30,
            'calories_per_serving': 350,
            'ingredients': [
                f'2 cups {ingredients}',
                '1 onion, diced',
                '2 cloves garlic, minced',
                'Salt and pepper to taste',
                '2 tbsp olive oil'
            ],
            'cuisine_type': 'International',
            'meal_type': 'Lunch',
            'diet_labels': ['Balanced'],
            'health_labels': ['Dairy-Free'],
        },
        {
            'title': f'Quick {ingredients} Stir-fry',
            'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=300&h=200&fit=crop',
            'source_url': 'https://example.com/recipe2',
            'servings': 2,
            'prep_time': 15,
            'calories_per_serving': 280,
            'ingredients': [
                f'1 lb {ingredients}',
                '2 tbsp vegetable oil',
                '1 bell pepper, sliced',
                '2 tbsp soy sauce',
                '1 tsp ginger, minced'
            ],
            'cuisine_type': 'Asian',
            'meal_type': 'Dinner',
            'diet_labels': ['High-Protein'],
            'health_labels': ['Gluten-Free'],
        }
    ]
    
    return {
        'success': True,
        'recipes': mock_recipes,
        'total_results': len(mock_recipes)
    }