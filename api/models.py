from django.db import models

# Create your models here.

class File(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="/origin_image/")

    def __str__(self):
        return self.image
