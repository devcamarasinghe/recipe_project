import requests
from decouple import config

def test_edamam_api():
    app_id = config('EDAMAM_APP_ID')
    app_key = config('EDAMAM_APP_KEY')
    
    print(f"App ID: {app_id[:10]}...")
    print(f"App Key: {app_key[:10]}...")
    
    # Updated API endpoint (v2)
    url = "https://api.edamam.com/api/recipes/v2"
    
    # Required headers
    headers = {
        'Edamam-Account-User': app_id,  # Use app_id as userID
        'Accept': 'application/json'
    }
    
    params = {
        'type': 'public',
        'q': 'chicken',
        'app_id': app_id,
        'app_key': app_key,
        'from': 0,
        'to': 5,
    }
    
    try:
        print(f"Testing URL: {url}")
        response = requests.get(url, params=params, headers=headers, timeout=15)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Success! Number of hits: {len(data.get('hits', []))}")
            
            # Show first recipe title if available
            if data.get('hits'):
                first_recipe = data['hits'][0]['recipe']
                print(f"First recipe: {first_recipe.get('label', 'No title')}")
            
            return True
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text[:500]}...")
            return False
            
    except Exception as e:
        print(f"Exception: {e}")
        return False

if __name__ == "__main__":
    test_edamam_api()