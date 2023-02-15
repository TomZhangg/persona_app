from django.contrib import admin

# Register your models here.
from .models import Persona

# Make persona class available to admin
admin.site.register(Persona)