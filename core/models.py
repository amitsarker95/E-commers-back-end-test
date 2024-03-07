from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if email is None:
            raise ValueError('You must specify an email address')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, password=None):
        if email is None:
            raise ValueError('You must specify an email address')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class Customer(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    location = models.TextField()
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self) -> str:
        return f"{self.username}" 



