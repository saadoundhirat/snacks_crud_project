from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=512, default='' )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("snack_detail", args=[str(self.id)])