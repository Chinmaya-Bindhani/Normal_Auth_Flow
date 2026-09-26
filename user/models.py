from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password,**extra_fields):
        if not email:
            raise ValueError('Email required ')

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,username,password,**extra_fields)



# custom class to execute the authentication by email and password
class CustomUserModel(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=200,unique=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    def __str__(self):
        return self.username
