from django.db import models

# Create your models here.
class ViewCount(models.Model):
    #fields you need
    
    user_id=models.IntegerField(default=0)
    surprise_id=models.IntegerField(default=0)
    count=models.IntegerField(default=0)

class overallView(models.Model):
    #fields you need
    all_count=models.IntegerField(default=0)