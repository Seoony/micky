from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
    def create_user(self, email,  password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        
        user = self.model(
            email=self.normalize_email(email),
            #name = name,
            #lastname = lastname,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,  password):
        user = self.create_user(email,  password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserMicky(AbstractBaseUser, PermissionsMixin):
    SEX_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    email = models.EmailField(max_length=127, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    dni = models.CharField(max_length=8, blank=True, null=True)
    #img = models.ImageField(upload_to='images/user')
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS)
    phone = models.CharField(max_length=12, blank=True)
    #district = models.CharField(max_length=64, choices=)
    #address = models.CharField(max_length=256, blank=True)
    #vip = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email  
