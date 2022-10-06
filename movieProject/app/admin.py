from django.contrib import admin
from . import models 


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['date', 'name', 'hero', 'heroine', 'rating']
