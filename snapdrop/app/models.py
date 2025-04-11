from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    def set_password(self,raw_password):
        self.password = make_password(raw_password)
        self.save()
    def check_password(self, raw_password):
        return check_password(raw_password,self.password)

class SignUp(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)