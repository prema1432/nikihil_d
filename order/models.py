# from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

# crud == create , read , update delete==

class my_places(models.Model):
    role_choices = (
        ('customer', 'customer'),
        ('manager', 'manager'),
        ('student', 'student'),
    )
    location_name = models.CharField(max_length=50)
    # iph =
    location_description = models.TextField()
    location_image = models.ImageField(upload_to="place_images", blank=True, null=True)
    # None,""
    age = models.IntegerField()
    gender = models.BooleanField(default=False)
    # false == women, true == men
    role = models.CharField(max_length=50, choices=role_choices, default="student")

    price = models.PositiveIntegerField(default=1)

    sub_total = models.FloatField(default=5)
    interests = models.JSONField(null=True, blank=True, default=list)

    # list_of_places = ArrayField
    website = models.URLField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    joined = models.DateField(null=True, blank=True)

    birthday = models.DateTimeField(null=True, blank=True)

    # forrrignkey == student , school == schol - -- students,, studen == school - student ,
    # many to many key == student, teachers ==> school== class table ==>
    # one to one == s

    def __str__(self):
        # return self.location_name
        return f"{self.id} - {self.location_name}"
