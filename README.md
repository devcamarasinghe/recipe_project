# Recipe Finder & Meal Planner

A Django web application that helps users find recipes based on available ingredients and plan their meals using the Edamam Recipe Search API.

Live site: [https://camarasinghe.pythonanywhere.com](https://camarasinghe.pythonanywhere.com)

## Features

- 🔍 Smart recipe search based on available ingredients
- 📊 Detailed nutritional information
- 🍽️ Recipe cards with images and cooking details
- 📱 Responsive design
- 🔗 Direct links to full recipes

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 4.0+
- Edamam API credentials

### Installation & Running Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/recipe-finder-meal-planner.git
   cd recipe-finder-meal-planner
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root with your Edamam API credentials:
     ```env
     EDAMAM_APP_ID=your_app_id
     EDAMAM_APP_KEY=your_app_key
     ```

5. **Apply migrations to set up the database:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

### Deployment (PythonAnywhere)

1. **Upload your project files (excluding local venv and db.sqlite3 if you want a fresh database).**
2. **Create a new virtual environment on PythonAnywhere and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
5. **Configure your web app (working directory, WSGI file, static files) in the PythonAnywhere dashboard.**
6. **Reload your web app.**

## Usage
- Enter ingredients to find recipes.
- View nutritional info and cooking instructions.
- Log in to the admin site at `/admin` to manage recipes and users.

## License
MIT
