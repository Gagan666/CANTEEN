from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

# Create your models here.
class CreateAccount(BaseUserManager):

    def create_user(self,phone,user_name,password,**other_fields):

        if not phone:
            raise ValueError("Enter Phone Number")
        other_fields.setdefault('is_active', True)
        user = self.model(phone=phone,user_name=user_name,password=password,**other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,phone,user_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        return self.create_user(phone=phone,user_name=user_name,password=password,**other_fields)


class NewUser(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(max_length=10,unique=True)
    user_name = models.CharField(max_length=100,blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD="phone"
    REQUIRED_FIELDS = ['user_name']
    objects = CreateAccount()