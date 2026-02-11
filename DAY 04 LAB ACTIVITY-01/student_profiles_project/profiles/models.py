<<<<<<< HEAD
from django.db import models

# Create your models here.
# Model to store student details
class Student(models.Model):
    name = models.CharField(max_length=100)       # Student's full name
    age = models.IntegerField()                   # Student's age
    course = models.CharField(max_length=100)     # Course enrolled
    email = models.EmailField()                   # Contact email
    def __str__(self):
        return self.name
=======
from django.db import models

# Create your models here.
# Model to store student details
class Student(models.Model):
    name = models.CharField(max_length=100)       # Student's full name
    age = models.IntegerField()                   # Student's age
    course = models.CharField(max_length=100)     # Course enrolled
    email = models.EmailField()                   # Contact email
    def __str__(self):
        return self.name
>>>>>>> 86c0bec (Initial commit with large folder)
