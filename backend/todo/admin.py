from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from todo.models.task.model import (
    Task
)

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    ordering = ['user']
    fieldsets = (
        (_("New task".upper()), {
            "fields": (
                'user',
                'title',
                'description',
            ),
        }),
    )

    list_display = ('title', 'user', 'created_date')
    search_fields = ('title', 'description')


admin.site.register(Task, TaskAdmin)