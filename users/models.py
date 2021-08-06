from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class MyUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+7999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=16,
                                    null=True,
                                    blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return f'{self.pk} - {self.username}'
