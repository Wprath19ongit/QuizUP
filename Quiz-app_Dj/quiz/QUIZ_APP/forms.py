from django.forms import ModelForm
from .models import *

class usersForm(ModelForm):
    class Meta:
        model = users
        # fields = ['username', 'password', 'first_name', 'last_name', 'email_id', 'reg_time']
        fields = '__all__'