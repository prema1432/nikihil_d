"""
URL configuration for maytoday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from order.views import welcome, abouts, contactus, locations, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include('order.urls')),
    path("", welcome, name="home"),
    # path("abouts/", abouts,name="about"),
    # path("contactus/", contactus,name="contact"),
    # path("locations/", locations,name="locations"),
    # path("login/", login,name="login"),
]

# base coammnds
# python manage.py runserver -- running project
# python manage.py makemigrations -- converting orm to sql
# python manage.py migrate -- appliying migration files
# python manage.py createsuperuser  -- createsuperuser
# python manage.py collectstatic -- collect static files stored in our databases


# creating application
