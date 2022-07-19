from django.contrib.auth.models import UserManager
from django.forms import ValidationError


class CustomUserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValidationError({'details': 'Email must be set'})

        email = self.normalize_email(email = email)
        user = self.model(email = email)
        user.set_password()
        user.save()
        
        return user
