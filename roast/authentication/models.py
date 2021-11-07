import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,password=None):

        if not email:
            raise ValueError('Must have an email')
        user = self.model(email=self.normalize_email)
        user.set_password(password)
    def create_superuser(self,email,password):
        if password is None:
            raise TypeError('SuperUsers must have a pwd')
        user=self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True

class User(AbstractBaseUser):
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email