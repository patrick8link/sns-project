from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Discovery(models.Model):
	ig_id = models.BigIntegerField(primary_key=True)
	username = models.CharField(max_length=255,null=False, blank=True)
	name = models.CharField(max_length=255,null=False, blank=True)
	profile_picture_url = models.CharField(max_length=2000,null=False,blank=True)
	follows_count = models.IntegerField(null=False,blank=True)
	followers_count = models.IntegerField(null=False,blank=True)
	media_count = models.IntegerField(null=False, blank=True)
	id = models.CharField(max_length=255,null=False, blank=True)

	def save(self, *args, **kwargs):
		return super(Customer, self).save(*args, **kwargs)

	def __unicode__(self):
		return "{}:{}".format(self.username,self.name)
