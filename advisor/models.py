from django.db import models
from django.conf import settings
    

class Advisor(models.Model):
    advisor_name = models.CharField(max_length = 60, unique=True)
    photo_url = models.URLField(max_length = 200)
        
    def __str__(self):
        return self.id

    