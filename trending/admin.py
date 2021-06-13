from django.contrib import admin
from .models import Trending

class TrendingAdmin(admin.ModelAdmin):
    list_display = ('date','title', 'author','description' ,'link','imgsrc')
# Register your models here.

admin.site.register(Trending, TrendingAdmin)