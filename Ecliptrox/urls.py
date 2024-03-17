from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.Welcome_to_Digital_Conscious),
    path('add-story/', views.add_story, name='add_story'),  # This is our new pat
    # also add this
    
    path('stories/', views.story_list, name='stories'),
    path('API_Stories/', views.API_Stories, name='API_Stories'),
    path('Finance_Python-stories/', views.Finance_Python_Stories, name='Finance_Python_Stories'),
    path('Cyber_Crime-stories/', views.Cyber_Crime_Stories, name='Cyber_Crime_Stories'),
    path('AI_Python-stories/', views.AI_Python_Stories, name='AI_Python_Stories'),
    # Add other paths as needed
]   
    