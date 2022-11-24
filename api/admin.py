from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser,Foods,Categories


# Register your models here.


class UserAdminConfig(UserAdmin):
    ordering = ("-start_date",)
    list_display = ('phone', 'user_name', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('phone', 'user_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Categories)
admin.site.register(Foods)
