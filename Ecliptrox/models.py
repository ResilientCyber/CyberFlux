from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    
class AI_Stories(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class API_Stories(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()    
    
class Cyber_Crime_Stories(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  
    
class Finance_Python_Stories(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()          