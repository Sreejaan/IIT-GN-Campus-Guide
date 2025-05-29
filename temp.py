import os
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CampusGuide.settings')  # Replace with your settings module
django.setup()

from core.models import Facility  # Replace with your actual app name if different

# List of parking areas to be added
parking_data = [
    {
        "name": "Academic Block Parking",
        "description": "Open parking near the academic buildings. Used by faculty, staff, and students.",
        "location_note": "Near Academic Block main entrance.",
        "google_maps_url": "https://maps.google.com/?q=23.2151015,72.6822127",
    },
    {
        "name": "Aibaan Hostel Parking",
        "description": "Designated parking for residents of Aibaan Hostel. Mainly used for two-wheelers.",
        "location_note": "Outside Aibaan Hostel main gate.",
        "google_maps_url": "https://maps.google.com/?q=23.2108546,72.6837397",
    },
    {
        "name": "Duven Hostel Parking",
        "description": "Two-wheeler parking area for Duven Hostel residents.",
        "location_note": "Beside Duven Hostel side entrance.",
        "google_maps_url": "https://maps.google.com/?q=23.2109455,72.6856043",
    },
    {
        "name": "Parking Near Sports Complex",
        "description": "Spacious parking lot near the sports complex. Often used during sports events.",
        "location_note": "Behind the sports complex building.",
        "google_maps_url": "https://maps.google.com/?q=23.2123451,72.6842102",
    },
    {
        "name": "Main Gate Parking",
        "description": "Primary parking space near the main entrance. Open for visitors and deliveries.",
        "location_note": "Just inside the main entrance gate.",
        "google_maps_url": "https://maps.google.com/?q=23.2134567,72.6812345",
    },
]

# Populate Facility model with parking data
def populate_parking_facilities():
    for facility in parking_data:
        slug = slugify(facility["name"])
        obj, created = Facility.objects.get_or_create(
            name=facility["name"],
            type="parking",
            defaults={
                "slug": slug,
                "description": facility["description"],
                "location_note": facility["location_note"],
                "google_maps_url": facility["google_maps_url"],
            }
        )
        if created:
            print(f"✅ Added: {facility['name']}")
        else:
            print(f"ℹ️ Already exists: {facility['name']}")

if __name__ == "__main__":
    populate_parking_facilities()
