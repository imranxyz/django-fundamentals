from django.contrib import admin
from . import models

@admin.register(models.Hydjobs)
class HydJobsAdmin(admin.ModelAdmin):
	list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


@admin.register(models.Punejobs)
class PuneJobsAdmin(admin.ModelAdmin):
	list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


@admin.register(models.Blorejobs)
class BangloreJobsAdmin(admin.ModelAdmin):
	list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


@admin.register(models.Kolkatajobs)
class KolkataJobsAdmin(admin.ModelAdmin):
	list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']
