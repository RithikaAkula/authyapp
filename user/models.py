from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authy.settings')


class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):
        
        if name is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(db_index=True, max_length=60, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

