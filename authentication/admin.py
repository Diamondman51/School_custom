from django.contrib import admin

from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_active', 'is_staff', 'is_admin')


admin.site.register(User, UserAdmin)