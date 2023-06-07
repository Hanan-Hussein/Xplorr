from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns=[
    
    path('all_countries/',views.allCountry.as_view(), name='countries'),
    path('all_cities/',views.allCities.as_view(), name='cities'),
    path('all_goals/',views.allGoals.as_view(), name='goals'),
    path('all_accomodations/',views.allAccomodations.as_view(), name='accomodations'),
    path('all_sightseeing/',views.allSightSeeing.as_view(), name='sightseeing'),
    path('all_categories/', views.allCategories.as_view(), name='categories'),

]
