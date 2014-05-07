from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('M', 'Maintenance'),
        ('D', 'Defunct'),
)

OS_CHOICES = (
        ('W', 'Windows'),
        ('M', 'OS X'),
        ('L', 'Linux'),
	('O', 'Other See Details'),
)

MOS_CHOICES = (
        ('A', 'Android'),
        ('I', 'iOS'),
        ('W', 'Windows Mobile'),
        ('O', 'Other See Details'),
)
class Asset(models.Model):
        #general information
        model = models.CharField(max_length=30)
        model_details = models.CharField(max_length=30)
        colour = models.CharField(max_length=30)
        created_date = models.DateField(auto_now_add=True)
        #assignedto
        assigned_to = models.CharField(max_length=20)
        program = models.CharField(max_length=100)
        #purchase information
        purchase_date = models.DateField()
        purchase_price = models.IntegerField(default=0)
        bought_from = models.CharField(max_length=100)
        warranty_info = models.TextField()
        status = models.CharField(max_length=1,
                                      choices=STATUS_CHOICES,
                                      default='I')
	notes = models.TextField()
	
	def __unicode__(self):
		return self.item

class Computer(models.Model):
	asset = models.OneToOneField(Asset, primary_key=True)
	os = models.CharField(max_length=1, choices=OS_CHOICES)
	os_version = models.CharField(max_length=10)
	win_key = models.CharField(max_length=20)
	computer_name = models.CharField(max_length=20)
	backup = models.CharField(max_length=20)
	serial = models.CharField(max_length=20)
	def __unicode__(self):
                return u"%s the computer" % (self.asset.model, self.asset.model_details)

class Phone(models.Model):
        asset = models.OneToOneField(Asset, primary_key=True)
	os = models.CharField(max_length=1, choices=MOS_CHOICES)
	os_version = models.CharField(max_length=10)
	imei = models.CharField(max_length=20)
	sim_num = models.CharField(max_length=20)
	phone_num = models.CharField(max_length=20)
	case = models.BooleanField()
	backup = models.CharField(max_length=20)
	serial = models.CharField(max_length=20)
	def __unicode__(self):
                return u"%s the phone" % (self.asset.model, self.asset.model_details)

class Tablet(models.Model):
        asset = models.OneToOneField(Asset, primary_key=True)
	os = models.CharField(max_length=1, choices=MOS_CHOICES)
	os_version = models.CharField(max_length=10)
	case = models.BooleanField()
	backup = models.CharField(max_length=20)
	serial = models.CharField(max_length=20)
        def __unicode__(self):
                return u"%s the tablet" % (self.asset.model, self.asset.model_details)
	
class Ticket(models.Model):
	asset = models.ForeignKey(Asset)
	title = models.CharField(max_length=20)
        content = models.TextField()
	resolved = models.BooleanField()
	created_date = models.DateField(auto_now_add=True)
	position = models.PositiveSmallIntegerField("Position")
	class Meta:
                ordering = ['position']
	def __unicode__(self):
		return self.title
