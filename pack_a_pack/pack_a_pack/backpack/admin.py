from django.contrib import admin
from .models import Trip, Backpack, Item, Profile
# Register your models here.

admin.site.register(Trip)
admin.site.register(Backpack)
admin.site.register(Item)
admin.site.register(Profile)