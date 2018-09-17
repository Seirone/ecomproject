from django.db import models

#app_name = 'profiles'

class profile(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(default='description default text')

	def __unicode__(self):
		return self.name
