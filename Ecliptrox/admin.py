from django.contrib import admin

# Register your models here.
from .models import Story  # This is our treasure chest
from .models import AI_Stories  # Import your AnotherStory model
from .models import API_Stories
from .models import Cyber_Crime_Stories
from .models import Finance_Python_Stories

admin.site.register(Story)  # This tells the guards about it

# Register the AnotherStory model with the admin site
admin.site.register(AI_Stories)
admin.site.register(API_Stories)
admin.site.register(Cyber_Crime_Stories)
admin.site.register(Finance_Python_Stories)