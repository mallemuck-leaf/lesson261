from django.contrib import admin
from .models import Project, Task

# Register your models here.


# class ProjectInline(admin.TabularInline):
#     model = Project
#     extra = 0


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creation_date')
    list_filter = ('creation_date',)
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id_project', 'description', 'creation_date', 'status', 'priority')
    list_filter = ('id_project', 'creation_date')
    fields = ('id_project', 'description', ('status', 'priority'))
    # inlines = [ProjectInline]

