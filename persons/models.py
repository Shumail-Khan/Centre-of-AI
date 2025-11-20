from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    face_encoding = models.JSONField()  # Store face encoding as a string

    def __str__(self):
        return self.name
