# from django.db import models
#
# # Create your models here.
# class Person(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     institution = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     sex = models.CharField(max_length=10)
#     country = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.firstname +' '+self.lastname
#
# class Workshop(models.Model):
#     workshop_name = models.CharField(max_length=100)
#     # date = models.DateTimeField(auto_now=True)
#     venue = models.CharField(max_length=50)
#     workshop_sponsor = models.CharField(max_length=50)
#
#
#     def __str__(self):
#         return self.workshop_name
#
#
# class Instructor(models.Model):
#     workshop_id = models.ForeignKey(Workshop,on_delete=models.CASCADE)
#     person_id = models.ForeignKey(Person,on_delete=models.CASCADE)
#     module_taught = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.module_taught
#
#
#
#
# MALE, FEMALE = range(2)
# GENDER = (
#     (MALE, 'MALE'),
#     (FEMALE, 'FEMALE')
# )
#
# class Attendees(models.Model):
#     full_name = models.CharField('Full Name', max_length=50)
#     gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
#     grades = models.CharField('Grades', max_length=2)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = ('Attendees')

from django.db import models

# Create your models here.

MAX_CHAR_LENGTH = 100


class Workshop(models.Model):

    name = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Name", null=True)
    start_date = models.DateField(db_column="Start_Date", null=True)
    end_date = models.DateField(db_column="End_Date", null=True)
    venue = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Venue", null=True)
    # sponsors= models.ForeignKey('Sponsor', on_delete=models.CASCADE,
    #                                        db_column="Workshop_Sponsored")
    # banner = models.ImageField(db_column="Workshop_Banner", null=True)

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
    institution = models.CharField(max_length=MAX_CHAR_LENGTH,
                                   db_column="Institution",default='')
    gender = models.CharField(max_length=1, db_column="Gender",
                              choices=GENDER_CHOICES,default='')
    country = models.CharField(max_length=MAX_CHAR_LENGTH,
                               db_column="Country",default='')

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



