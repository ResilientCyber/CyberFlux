from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StoryForm
from .models import Story
# from django.http import HttpResponse

# Create your views here.


def Welcome_to_Digital_Conscious(request):
    return render(request, "Ecliptrox/Welcome_to_Digital_Conscious.html")

def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story_list')  # Take them to see all stories after sharing theirs
    else:
        form = StoryForm()  # Create an empty form for a new story
    return render(request, 'Ecliptrox/add_story.html', {'form': form})
    pass

def story_list(request):
    stories = Story.objects.all()  # This collects all the stories from the vault
    return render(request, 'Ecliptrox/story_list.html', {'stories': stories})

def API_Stories(request):
    # Your view logic here
    #return HttpResponse("API stories view")
    stories = Story.objects.all()  # This collects all the stories from the vault
    return render(request, 'Ecliptrox/API_stories.html', {'stories': stories})

def Finance_Python_Stories(request):
    # Your view logic here
    #return HttpResponse("API stories view")
    stories = Story.objects.all()  # This collects all the stories from the vault
    return render(request, 'Ecliptrox/Finance_Python_stories.html', {'stories': stories})

def Cyber_Crime_Stories(request):
    # Your view logic here
    #return HttpResponse("API stories view")
    stories = Story.objects.all()  # This collects all the stories from the vault
    return render(request, 'Ecliptrox/Cyber_Crime_stories.html', {'stories': stories})

def AI_Python_Stories(request):
    # Your view logic here
    #return HttpResponse("API stories view")
    stories = Story.objects.all()  # This collects all the stories from the vault
    return render(request, 'Ecliptrox/AI_Python_stories.html', {'stories': stories})