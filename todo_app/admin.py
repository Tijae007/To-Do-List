from django.contrib import admin
from todo_app.models import TaskList

# Register your models here.
admin.site.site_header = 'TO-DO-LIST DESIGN'
admin.site.register(TaskList)