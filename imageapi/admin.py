from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.UserResponse)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_response', 'response_image']

