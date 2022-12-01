from django.contrib import admin

# Register your models here.
from . import models
#items to be displayed on the admin panel
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'publish')

admin.site.register(models.Post, AuthorAdmin)