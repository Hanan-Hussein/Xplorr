from django.contrib import admin
from .models import Country, City, Goals, Profile, Accomodation, Sightseeing
# Register your models here.

class countryAdmin(admin.ModelAdmin):
    list_display =("name", "iso", "code")
    list_filter =("name","code")

class cityAdmin(admin.ModelAdmin):
    list_display=("name", "country")

class goalsAdmin(admin.ModelAdmin):
    list_display = ("goalName", "moneySaved", "user", "city")

class profileAdmin(admin.ModelAdmin):
    list_display=("user","profile_image")

class accomodationAdmin(admin.ModelAdmin):
    list_display=("name","location", "city", "price")
    list_filter = ("city", "price")

class sightSeeAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "city", "price")
    list_filter =("price", "location")

all = [(Country,countryAdmin),(City,cityAdmin),
(Goals,goalsAdmin),(Profile,profileAdmin),(Accomodation,accomodationAdmin),(Sightseeing, sightSeeAdmin)]

for i in all:
    admin.site.register(i[0],i[1])
