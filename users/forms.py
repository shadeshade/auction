from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        ]
