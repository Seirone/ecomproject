from django.db import models

#app_name = 'contact'

class contactForm(models.Model):   	
	name = models.CharField(max_length=100, help_text='100 characters max.')
	email = models.EmailField(max_length=100)
	comment = models.CharField(max_length=1000, default=False)

	def __str__(self):
		return self.name