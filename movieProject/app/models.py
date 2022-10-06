from django.db import models

class Movie(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=50)
	hero = models.CharField(max_length=50)
	heroine = models.CharField(max_length=50)
	rating = models.IntegerField()

	def __str__(self):
		return self.name
