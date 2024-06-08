
from django.urls import path

from order.views import abouts, locations, login, contactus, create_new_places

urlpatterns = [
    path("abouts/", abouts,name="about"),
    path("contactus/", contactus,name="contact"),
    path("locations/", locations,name="locations"),
    path("login/", login,name="login"),
    path("create_place",create_new_places,name="create_new_place"),
]