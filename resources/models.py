from django.db import models

# Create your models here.
class Classroom(models.Model):
    block = models.CharField(max_length=10)
    capacity = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.IntegerField()
