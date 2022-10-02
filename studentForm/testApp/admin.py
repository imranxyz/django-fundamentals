from django.contrib import admin
from . import models 

admin.site.site_header = 'Student Registration Panel'  # default: "Django Administration"
admin.site.index_title = 'Registration Forms' # default: "Site administration"
admin.site.site_title = 'Registration Dashboard' # default: "Django site admin"

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'marks']
