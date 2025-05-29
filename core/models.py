from django.db import models
from django.utils.text import slugify

class Building(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50)  # e.g., 'hostel'
    google_maps_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.IntegerField()
    label = models.CharField(max_length=50)  # e.g. "Ground Floor"

    def __str__(self):
        return f"{self.building.name} - {self.label}"

class Location(models.Model):
    TYPE_CHOICES = [
        ("room", "Room"),
        ("washroom", "Washroom"),
        ("common_room", "Common Room"),
        ("water", "Water Cooler"),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    direction_note = models.TextField()
    google_maps_url = models.URLField(blank=True, help_text="Optional: Link to this specific place on Google Maps")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.floor.building.name}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
from django.db import models

class CampusCategory(models.Model):
    title = models.CharField(max_length=100)
    emoji = models.CharField(max_length=5)
    description = models.TextField()
    url_name = models.CharField(max_length=100, blank=True)
    button_value = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title


class Shop(models.Model):
    SHOP_TYPES = [
        ("stationery", "Stationery"),
        ("food", "Food & Snacks"),
        ("printing", "Printing"),
        ("general", "General Store"),
        ("others", "Others"),
        ("mess", "Mess"),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    type = models.CharField(max_length=20, choices=SHOP_TYPES, default="others")
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=50, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True, help_text="e.g. 9AM - 7PM")
    location_note = models.TextField(blank=True, help_text="E.g. Near Hostel B main gate")
    google_maps_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Facility(models.Model):
    FACILITIES_TYPES = [
        ("auditorium", "Auditorium"),
        ("adventure", "Adventure Spot"),
        ("bank", "Bank and ATM"),
        ("health", "Health Center"),
        ("parking", "Parking Area"),
        ("faculty", "Faculty Room"),
        ("sports", "Sports"),
        ("other", "Other"),
    ]

    # Common fields
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    type = models.CharField(max_length=20, choices=FACILITIES_TYPES, default="other")
    description = models.TextField(blank=True)
    mobile_number = models.CharField(max_length=100, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)
    location_note = models.TextField(blank=True)
    google_maps_url = models.URLField(blank=True)
    more_info_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Optional/specific fields for Auditorium
    capacity = models.IntegerField(blank=True, null=True)
    has_projector = models.BooleanField(default=False)
    sound_system_brand = models.CharField(max_length=100, blank=True)

    # Optional/specific fields for Bank
    ifsc_code = models.CharField(max_length=20, blank=True)
    branch_code = models.CharField(max_length=20, blank=True)
    atm_available = models.BooleanField(default=False)

    # Optional/specific fields for Faculty Room
    faculty_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    office_hours = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

