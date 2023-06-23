from django.contrib import admin
from .models import *
admin.site.site_header='Views counter'


# Register your models here.
prepopulated_fields = {'slug': ('title',)}
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}