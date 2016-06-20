# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from . import helpers


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, years,
                    weight, height,
                    password=None, is_superuser=False):
        if not email:
            raise ValueError('Users must have an email address')

        BMI = int(weight) / ((int(height) / 100)**2)
        calc_cal = helpers.\
            max_calories(int(height), int(weight), int(years), gender)

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            years=years,
            weight=weight,
            height=height,
            BMI=BMI,
            max_cal=calc_cal,
            is_superuser=is_superuser
        )
        if password is None:
            password = self.make_random_password()

        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        return self.create_user(email, name, password, is_superuser=True)

    def create(self, *args, **kwargs):
        return self.create_user(*args, **kwargs)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    years = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    BMI = models.FloatField(default=0)
    max_cal = models.FloatField(default=0)

    is_active = models.BooleanField(default=True)

    @classmethod
    def exists(cls, email):
        try:
            cls.objects.get(email=email)
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def login_user(cls, email, password):
        try:
            u = cls.objects.get(email=email, password=password)
            return u
        except cls.DoesNotExist:
            return None

    @property
    def is_staff(self):
        return self.is_superuser

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.email
