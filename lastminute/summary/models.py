from django.db import models


class Lecture(models.Model):
    Name = models.TextField()
    date = models.DateField()
    professor = models.TextField()
    transcript = models.TextField()
    thumbnail = models.TextField()
    hidden = models.BooleanField()

