from django.forms import ModelForm
from .models import *

class Todo_Form(ModelForm):
    class Meta:
        model = Todu
        fields =['titla','text','date']