from django.forms import ModelForm
from .models import Tasting

class TastingForm(ModelForm):
  class Meta:
    model = Tasting
    fields = ['date', 'time']