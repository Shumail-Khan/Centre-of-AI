from django.db import models
import json

class Person(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    face_encoding = models.JSONField()   # stores list of floats

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
