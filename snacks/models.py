from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey('auth.User', related_name='snacks', on_delete=models.CASCADE)
    description = models.TextField(max_length=512, default='' )

    def __str__(self):
        return self.title