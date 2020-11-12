from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
	filter_horizontal=('classes',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Class)
admin.site.register(ProfileClass)
