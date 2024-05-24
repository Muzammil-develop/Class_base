from django.db import models

# Create your models here.

class Blog (models.Model):
    writer = models.CharField (max_length=50)
    article = models.CharField (max_length=120)
    active = models.BooleanField (default=False)

    def __str__(self):
        return self.writer
    
    
