import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CampusGuide.settings')  # Use your project name here
django.setup()

# Now you can import models
from core.models import CampusCategory

# Example: create a new category
# from core.models import Category


categories = [
    {"title": "Academic", "emoji": "🎓", "description": "Find classrooms, departments and labs.", "button_value": "Go to Academic", "url_name": "academic_index"},
    {"title": "Adventure", "emoji": "🧗", "description": "Explore open-air activities and adventurous spots.", "button_value": "Explore Adventure", "url_name": "adventure_index"},
    {"title": "Auditorium", "emoji": "🎤", "description": "Locate seminar halls and auditorium spaces.", "button_value": "Find Auditorium", "url_name": "auditorium_index"},
    {"title": "Bank & ATM", "emoji": "🏦", "description": "Locate campus ATMs and banking services.", "button_value": "Visit Bank/ATM", "url_name": "bank_atm_index"},
    {"title": "Faculty Office", "emoji": "🧑‍🏫", "description": "Find professor offices.", "button_value": "Go to Faculty Offices", "url_name": "faculty_office_index"},
    {"title": "Food", "emoji": "🍽️", "description": "Discover canteens, mess, and food courts.", "button_value": "Explore Food", "url_name": "food_index"},
    {"title": "Health Center", "emoji": "🏥", "description": "Find the medical room and emergency care.", "button_value": "Go to Health Center", "url_name": "health_center_index"},
    {"title": "Hostels", "emoji": "🏠", "description": "Locate hostels, washrooms, water coolers, and rooms.", "button_value": "Go to Hostels", "url_name": "hostel_index"},
    {"title": "Library", "emoji": "📚", "description": "Visit the central library and reading rooms.", "button_value": "Go to Library", "url_name": "library_index"},
    {"title": "Parking Area", "emoji": "🅿️", "description": "Find vehicle parking zones around campus.", "button_value": "Locate Parking", "url_name": "parking_area_index"},
    {"title": "Research Park", "emoji": "🧪", "description": "Explore innovation hubs and project centers.", "button_value": "Visit Research Park", "url_name": "research_park_index"},
    {"title": "Shops", "emoji": "🛒", "description": "Stationery, printing, general campus stores.", "button_value": "Browse Shops", "url_name": "shops_index"},
    {"title": "Sports", "emoji": "🏸", "description": "Access fields, courts, and sports facilities.", "button_value": "View Sports", "url_name": "sports_index"},
    {"title": "Washrooms", "emoji": "🚻", "description": "Locate restrooms across all blocks and hostels.", "button_value": "Find Washrooms", "url_name": "washrooms_index"},
    {"title": "Water Points", "emoji": "💧", "description": "View all water coolers across campus.", "button_value": "View Water Points", "url_name": "water_points_index"},
]


for cat in categories:
    CampusCategory.objects.create(**cat)
