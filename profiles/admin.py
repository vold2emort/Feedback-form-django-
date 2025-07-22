from django.contrib import admin
from .models import UserProfiles

# Register your models here.
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(UserProfiles, UserProfilesAdmin)