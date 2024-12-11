from django.db import models

import jwt
from jwt import PyJWT

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    objects = UserManager()
    
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        #return str(refresh.access_token)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
