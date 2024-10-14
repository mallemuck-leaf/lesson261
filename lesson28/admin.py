from django.contrib import admin
from .models import User, Task

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_mail', 'password')
    list_filter = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'executor', 'status', 'created_date', 'completed_date')
    list_filter = ('title', 'executor', 'status', 'created_date', 'completed_date')
    fields = ('title', 'description', ('executor', 'status'), ('completed_date',))
