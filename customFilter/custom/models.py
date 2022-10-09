from django.db import models

class FilterDemo(models.Model):
	name = models.CharField(max_length=50)
	subjects = models.CharField(max_length=50)
	age = models.IntegerField()
	date = models.DateField()

	def __str__(self):
		return self.name
