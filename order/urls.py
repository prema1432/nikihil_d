from django.urls import path

from order.views import abouts, locations, login_view, contactus, create_new_places, get_place, get_place_update, \
    place_delete, logout_view

urlpatterns = [
    path("abouts/", abouts, name="about"),
    path("contactus/", contactus, name="contact"),
    path("locations/", locations, name="locations"),
    path("login/", login_view, name="login"),
    path("create_place", create_new_places, name="create_new_place"),

    path("locations/<id>/", get_place, name="get_place"),
    path("locations_update/<id>/", get_place_update, name="get_place_update"),
    path("locations_delete/<id>/", place_delete,name="place_delete"),

    path("logout",logout_view,name="logout"),
]
