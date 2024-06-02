from django.contrib import admin

from order.models import my_places


# Register your models here.


# template inheritence
#
# ==> base == (Parent Template)
# ==> {% block ""} {% endblock %}
# ==> {% include '''''' %} == components
#
# ==> inheroirt the parent model ==> extends == parent html name
#
# ==> one ecommerce website
#
# ==> Rroute paths, css, and bootstrap, and applications
#
# ==>

@admin.register(my_places)
class my_placesADmin(admin.ModelAdmin):
    list_display = ['id']
