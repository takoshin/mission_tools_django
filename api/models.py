from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email address is must')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4,
                            primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class LostArticle(models.Model):

    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    
    STATE = (
        ('1', '保管'),
        ('2', '返却'),
        ('3', '廃棄'),
    )


    id = models.UUIDField(default=uuid.uuid4,
                            primary_key=True, editable=False)
    lost_article = models.CharField(max_length=50, blank=False)
    place = models.CharField(max_length=50, blank=False)
    discoverer = models.CharField(max_length=50, blank=False)
    customer = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(validators = [phone_number_regex], max_length = 16, blank=True, null=True)
    staff = models.CharField(max_length=50, blank=True)
    state = models.CharField(blank=False, max_length=10, choices=STATE, default=STATE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lost_article