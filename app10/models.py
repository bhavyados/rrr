from django.db import models

# Create your models here.
class rr(models.Model):
    per_id=models.IntegerField(primary_key=True)
    per_name=models.CharField(max_length=100)
