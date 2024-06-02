from django.db import models


# Create your models here.


class my_places(models.Model):
    location_name = models.CharField(max_length=50)
    location_description = models.TextField()
    location_image = models.ImageField(upload_to="place_images")


    def __str__(self):
        # return self.location_name
        return f"{self.id} - {self.location_name}"
