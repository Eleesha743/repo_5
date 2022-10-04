from django.contrib import admin
from testapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['title','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)
