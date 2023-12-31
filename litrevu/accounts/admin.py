from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UserFollow

UserModel = get_user_model()


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserFollow)
