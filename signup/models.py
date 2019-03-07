from django.db import models

class Student_login(models.Model):
    roll_no = models.IntegerField(primary_key = True)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)

    
