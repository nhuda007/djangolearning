from django.db import models

class Member(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    age= models.IntegerField()

    def __str__(self):
        return self.fname