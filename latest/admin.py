from django.contrib import admin
from .models import Latest

class LatestAdmin(admin.ModelAdmin):
    list_display = ('date','title', 'author','description' ,'link','imgsrc')
# Register your models here.

admin.site.register(Latest, LatestAdmin)