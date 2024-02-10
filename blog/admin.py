from django.contrib import admin
from .models import Post
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display = ['author', 'title' , 'date']
admin.site.register(Post,postadmin)
    