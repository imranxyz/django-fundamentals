from django.db import models


class Hydjobs(models.Model):
	date = models.DateField();
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	eligibility = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.IntegerField()

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = 'Hydjobs'


class Blorejobs(models.Model):
	date = models.DateField();
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	eligibility = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.IntegerField()

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = 'Blorejobs'


class Punejobs(models.Model):
	date = models.DateField();
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	eligibility = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.IntegerField()

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = 'Punejobs'


class Kolkatajobs(models.Model):
	date = models.DateField();
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	eligibility = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.IntegerField()

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = 'Kolkatajobs'

