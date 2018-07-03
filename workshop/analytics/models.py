from django.db import models
from django_countries.fields import CountryField

# Create your models here.

MAX_CHAR_LENGTH = 100


class Workshop(models.Model):

    name = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Name", null=True)
    start_date = models.DateField(db_column="Start_Date", null=True)
    end_date = models.DateField(db_column="End_Date", null=True)
    venue = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Venue", null=True)
   
    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    workshop_sponsored = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                           db_column="Workshop_Sponsored")

    def __str__(self):
        return self.name


class Track(models.Model):
    track_title = models.CharField(max_length=MAX_CHAR_LENGTH,
                                   db_column="Track_Title")
    associated_workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                            db_column="Associated_Workshop")

    def __str__(self):
        return self.track_title


class Institution(models.Model):
    institution_name = models.CharField(max_length=MAX_CHAR_LENGTH,
                                   db_column="Institution_name", null=True)
    location = models.CharField(max_length=MAX_CHAR_LENGTH,
                                   db_column="Location", null=True)
    def __str__(self):
        return self.institution_name


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    first_name = models.CharField(max_length=MAX_CHAR_LENGTH,
                                  db_column="First_Name",default='')
    last_name = models.CharField(max_length=MAX_CHAR_LENGTH,
                                 db_column="Last_Name",default='')
    email = models.EmailField(db_column="Email_Address",default='')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,
                                         db_column="Institution",default='')
    gender = models.CharField(max_length=1, db_column="Gender",
                              choices=GENDER_CHOICES,default='')
    country = CountryField(blank_label='select country', db_column="Country")
    
    def __str__(self):
        return self.first_name


class Attendee(Person):
    workshop_attended = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                          db_column="Workshop_Attended")

    def __str__(self):
        return self.first_name


class Instructor(Person):
    workshop_affiliated = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                            db_column="Workshop_Affiliated",default='')
    track_they_teach = models.ForeignKey(Track, on_delete=models.CASCADE,
                                         db_column="Track_They_Teach",default='')

    def __str__(self):
        return self.first_name



