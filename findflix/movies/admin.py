from django.contrib import admin
from .models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_filter = ('genre',) 

admin.site.register(Movie,MovieAdmin)


