from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
#     age = models.ForeignKey('Age', on_delete=models.CASCADE, default = 1)

# class Age(models.Model):
#     member_age = models.IntegerField()