from django.db import models

# Create your models here.
class DisneylandReview(models.Model):
    Review_ID = models.IntegerField()
    Rating = models.IntegerField()
    Year = models.IntegerField()
    Text = models.CharField(max_length=255)
    Branch = models.CharField(max_length=255)


