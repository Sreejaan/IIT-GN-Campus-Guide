import os
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CampusGuide.settings')  # Replace with your project's settings module
django.setup()

from core.models import Shop  # Replace with your app's name

# List of shops to be added
shops_data =[
     {
        "name": "Jaiswal Mess",
        "type": "mess",
        "description": "Ground Floor - Serves nutritious and hygienic food, including options for Jain meals, to the hostel community. The menu is curated monthly by the student mess council.",
        "owner": "",
        "mobile_number": "",
        "opening_hours": "7:30 AM - 9:30 AM, 12:15 PM - 2:15 PM, 4:30 PM - 6:00 PM ,7:30 PM - 9:30 PM",
        "location_note": "Located near Aibaan Hostel.",
        "google_maps_url": "https://www.google.com/maps/dir//23.2108067,72.683742/@23.2108802,72.6425422,13736m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDUyNi4wIKXMDSoASAFQAw%3D%3D"
    },
    {
        "name": "Mohani Mess",
        "type": "mess",
        "description": "First Floor - Serves nutritious and hygienic food, including options for Jain meals, to the hostel community. The menu is curated monthly by the student mess council.",
        "owner": "",
        "mobile_number": "",
        "opening_hours": "7:30 AM - 9:30 AM, 12:15 PM - 2:15 PM, 4:30 PM - 6:00 PM ,7:30 PM - 9:30 PM",
        "location_note": "Located near Aibaan Hostel.",
        "google_maps_url": "https://www.google.com/maps/dir//23.2108067,72.683742/@23.2108802,72.6425422,13736m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDUyNi4wIKXMDSoASAFQAw%3D%3D"
    },
    {
        "name": "RGouras Mess",
        "type": "mess",
        "description": "First Floor - Serves nutritious and hygienic food, including options for Jain meals, to the hostel community. The menu is curated monthly by the student mess council.",
        "owner": "",
        "mobile_number": "",
        "opening_hours": "7:30 AM - 9:30 AM, 12:15 PM - 2:15 PM, 4:30 PM - 6:00 PM ,7:30 PM - 9:30 PM",
        "location_note": "Located near Duven Hostel.",
        "google_maps_url": "https://www.google.com/maps/dir//23.2108202,72.6855757/@23.2108937,72.6443759,13736m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDUyNi4wIKXMDSoASAFQAw%3D%3D"
    },
]
# Function to populate the Shop model
def populate_shops():
    for shop in shops_data:
        slug = slugify(shop["name"])
        shop_instance, created = Shop.objects.get_or_create(
            name=shop["name"],
            defaults={
                "slug": slug,
                "type": shop["type"],
                "description": shop["description"],
                "owner": shop["owner"],
                "mobile_number": shop["mobile_number"],
                "opening_hours": shop["opening_hours"],
                "location_note": shop["location_note"],
                "google_maps_url": shop["google_maps_url"],
            }
        )
        if created:
            print(f"Added: {shop['name']}")
        else:
            print(f"Already exists: {shop['name']}")

if __name__ == "__main__":
    populate_shops()
