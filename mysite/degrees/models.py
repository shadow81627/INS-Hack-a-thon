from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Offering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trimester = models.IntegerField()
    def __str__(self):
        return self.course + self.trimester
