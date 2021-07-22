from django.forms import ModelForm

from .models import Store


class StoreModelForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name']
        labels = {'name': 'Store'}
