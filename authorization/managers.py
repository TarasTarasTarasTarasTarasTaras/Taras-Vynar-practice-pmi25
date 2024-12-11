import jwt

from datetime import datetime, timedelta

from django.conf import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password, **names):
        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password.')
        email=self.normalize_email(email)
        user = self.model(email=self.normalize_email(email), **names)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if _first_name is None:
            raise TypeError('Users must have a first name')
        
        if _last_name is None:
            raise TypeError('Users must have a last name')
        
        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(email=self.normalize_email(email), **names)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
