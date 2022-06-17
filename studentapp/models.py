from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    department_name= models.CharField(max_length=200)
    mobile = models.IntegerField()


class Dept(models.Model):
    department = models.ForeignKey(Student, on_delete=models.CASCADE)
