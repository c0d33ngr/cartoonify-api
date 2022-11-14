from django.db import models

# Create your models here.

class File(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="original-images/")

    def __str__(self):
        return self.description
