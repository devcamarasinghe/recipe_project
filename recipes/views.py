from django.shortcuts import render
from django.contrib import messages
from .services import search_recipes_api

def home(request):
    """Main page with search form"""
    return render(request, 'recipes/home.html')

def search_recipes(request):
    """Search for recipes using ingredients"""
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients', '').strip()
        
        if not ingredients:
            messages.error(request, 'Please enter some ingredients!')
            return render(request, 'recipes/home.html')
        
        # Call the API service
        result = search_recipes_api(ingredients)
        
        if result['success']:
            context = {
                'ingredients': ingredients,
                'recipes': result['recipes'],
                'total_results': result['total_results']
            }
            return render(request, 'recipes/search_results.html', context)
        else:
            messages.error(request, result['error'])
            return render(request, 'recipes/home.html')
    
    return render(request, 'recipes/home.html')