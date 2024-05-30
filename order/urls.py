
from django.urls import path

from order.views import abouts, locations, login, contactus

urlpatterns = [
    path("abouts/", abouts,name="about"),
    path("contactus/", contactus,name="contact"),
    path("locations/", locations,name="locations"),
    path("login/", login,name="login"),
]