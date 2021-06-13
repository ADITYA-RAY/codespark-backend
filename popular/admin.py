from django.contrib import admin
from .models import Popular

class PopularAdmin(admin.ModelAdmin):
    list_display = ('date','title', 'author','description' ,'link','imgsrc')
# Register your models here.

admin.site.register(Popular, PopularAdmin)