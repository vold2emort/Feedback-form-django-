from django.db import models

# Create your models here.
class UserProfiles(models.Model):
    # image = models.FileField(upload_to="images")
    image = models.ImageField(upload_to="images")