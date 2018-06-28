from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname +' '+self.lastname

class Workshop(models.Model):
    workshop_name = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=50)
    workshop_sponsor = models.CharField(max_length=50)
    workshop_logo = models.FileField()

    def __str__(self):
        return self.workshop_name + ' held on ' + self.date


class Instructor(models.Model):
    workshop_id = models.ForeignKey(Workshop,on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person,on_delete=models.CASCADE)
    module_taught = models.CharField(max_length=100)

    def __str__(self):
        return self.module_taught


class Attendee(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    workshop_id = models.ForeignKey(Workshop,on_delete=models.CASCADE)
