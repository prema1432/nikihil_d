from django import forms

from order.models import my_places


class my_placesform(forms.ModelForm):
    class Meta:
        model = my_places
        fields = '__all__'
        # fields =["location_name","age"]

