from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="components")
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, related_name="components"
    )
    name = models.CharField(max_length=200)
    part_number = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
