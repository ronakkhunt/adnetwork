from django.db import models

# Create your models here.


class Publisher(models.Model):
	
	username = models.CharField(max_length=20)
	apid = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=20)
	type = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username
