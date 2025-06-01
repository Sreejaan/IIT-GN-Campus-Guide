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



# Facility Model and data

from django.db import models
from django.utils.text import slugify

# ---- Departments ----
TYPE_CHOICES = [
    ('cse', 'Computer Science and Engineering'),
    ('electrical', 'Electrical Engineering'),
    ('civil', 'Civil Engineering'),
    ('mechanical', 'Mechanical Engineering'),
    ('chemical', 'Chemical Engineering'),
    ('materials', 'Materials Engineering'),
    ('biosciences', 'Biological Sciences and Bioengineering'),
    ('maths', 'Mathematics'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('humanities', 'Humanities and Social Sciences'),
    ('earth', 'Earth Sciences'),
    ('cognitive', 'Cognitive and Brain Sciences'),
    ('design', 'Design'),
    ('other', 'Staff/Other'),
]

DESIGNATION_CHOICES = [
    ('professor', 'Professor'),
    ('associate_professor', 'Associate Professor'),
    ('assistant_professor', 'Assistant Professor'),
    ('visiting_faculty', 'Visiting Faculty'),
    ('adjunct_professor', 'Adjunct Professor'),
    ('emeritus_professor', 'Emeritus Professor'),
    ('postdoc', 'Postdoctoral Fellow'),
    ('research_staff', 'Research Staff'),
    ('teaching_assistant', 'Teaching Assistant'),
    ('admin_staff', 'Administrative Staff'),
    ('director', 'Director'),
    ('dean', 'Dean'),
    ('hod', 'Head of Department'),
    ('warden', 'Warden'),
    ('other', 'Other'),
]


class Department(models.Model):
    code = models.CharField(max_length=50, choices=TYPE_CHOICES, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Designation(models.Model):
    code = models.CharField(max_length=50, choices=DESIGNATION_CHOICES, unique=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Role(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='roles')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)

    office_location = models.CharField(max_length=255, blank=True, null=True)
    accessibility_info = models.CharField(max_length=255, blank=True, null=True)
    office_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        person_name = self.person.name if self.person else "Unknown Person"
        designation_title = self.designation.title if self.designation else "No Designation"
        department_name = self.department.name if self.department else "No Department"
        return f"{person_name} - {designation_title} ({department_name})"
    

class MapStep(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='map_steps')
    step_number = models.PositiveIntegerField()
    map_embed_url = models.URLField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"{self.person.name} - Step {self.step_number}"
    
class WaterAndWashroom(models.Model):
    FACILITY_TYPES = [
        ('washroom', 'Washroom'),
        ('water_point', 'Water Point'),
        ('both', 'Both'),
    ]

    name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPES)
    google_maps_url = models.URLField()
    location_note = models.TextField(blank=True)
    building = models.CharField(max_length=50, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    accessibility = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.facility_type})"
