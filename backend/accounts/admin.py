from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from accounts.models.user_model import (
    User
)

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    ordering = ['first_name']

    fieldsets = (
        (
            _("User Data".upper()), {
                'fields': (
                    'email', 
                    'first_name', 
                    'last_name', 
                    'password',
                )
            }
        ),
        (
            _("Permissions".upper()), {
                "fields": (
                    'is_superuser',
                    'is_staff',
                ),
            }
        ),
        (
            _('Important dates'.upper()), {
                "fields": 
                (
                    "last_login",
                )
            }
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password',
            )
        })
    )

    readonly_fields = ['last_login']

    list_display = ['first_name', 'last_name', 'email', 'is_staff']

admin.site.register(User, UserAdmin)