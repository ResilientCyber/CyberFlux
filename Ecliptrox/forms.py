from django import forms
from .models import Story
from .models import AI_Stories
from .models import API_Stories
from .models import Cyber_Crime_Stories
from .models import Finance_Python_Stories


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']
        
        
class AIStoryForm(forms.ModelForm):
    class Meta:
        model = AI_Stories
        fields = ['title', 'content']        
        
        
class APIStoryForm(forms.ModelForm):
    class Meta:
        model = API_Stories
        fields = ['title', 'content']    
        
        
class CyberCrimeStoryForm(forms.ModelForm):
    class Meta:
        model = Cyber_Crime_Stories
        fields = ['title', 'content'] 
        
class FinancePythonStoryForm(forms.ModelForm):
    class Meta:
        model = Finance_Python_Stories
        fields = ['title', 'content']        
            