from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from registration.signals import user_registered

SERVICE_CHOICES = (
        ('FT', 'Full-time'),
        ('P3', 'Part-time 3 days per week'),
        ('P2', 'Part-time 2 days per week'),
        ('IT', 'Infant and Toddler Program (Birth to 3 years)'),
        ('35', 'Three to Five Program  (3 - 5 years)'),
)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),

)
class Family(models.Model):
    user = models.ForeignKey(User, unique=True)
    family_name = models.CharField(max_length=50, blank=True)
	
		
class Parent(models.Model):
    created_by = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cell_phone = models.IntegerField()
    work_phone = models.IntegerField()
    home_phone = models.IntegerField()
    contact_email = models.EmailField()
    signup_date = models.DateTimeField(auto_now_add=True)

class Centre(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    hours = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    services = models.CharField(max_length=2, choices=SERVICE_CHOICES)
    supervisor = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    info = models.TextField()
	
    signup_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
	return self.first_name

class Child(models.Model):
    #General Info
    created_by = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    #Booleans for Points
    special_needs = models.BooleanField()
    supported_child_dev = models.BooleanField()
    parent_at_baci = models.BooleanField()
    parent_at_ibm = models.BooleanField()
    sibling_enrolled = models.BooleanField()
    signup_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Children'

    def __unicode__(self):
	return self.first_name

class Application(models.Model):
    child = models.ForeignKey(Child)
    centre = models.ForeignKey(Centre)
    signup_date = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=2, choices=SERVICE_CHOICES)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    position = models.IntegerField()
    weight = models.IntegerField()
    comments = models.TextField()
    supevisor_notes = models.TextField()
	
def user_registered_callback(sender, user, request, **kwargs):
    profile = Family(user = user)
    profile.save()
 
user_registered.connect(user_registered_callback)
