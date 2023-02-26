from django.db import models


class Lecture(models.Model):
    Name = models.TextField()
    date = models.DateField()
    professor = models.TextField()
    transcript = models.TextField()
    thumbnail = models.TextField()
    hidden = models.BooleanField()

    def __str__(self):
        return f'Lecture:{self.Name}\nProfessor:{self.professor}\nDate:{self.date}\n'

    def get_all(self):
        pass