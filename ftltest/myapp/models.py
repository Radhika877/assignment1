from django.db import models

# Create your models here.
class user(models.Model):
    id = models.IntegerField(null=False,primary_key=True)
    real_name = models.CharField(max_length=30,null=False)
    tz = models.CharField(max_length=20,null=False)
    
    class Meta:
        db_table = 'user'
        
class activity_periods(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='activity_periods'
