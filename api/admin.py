from django.contrib import admin

from .models import *

class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages

class ProjectAdmin(admin.ModelAdmin):
    fields = ['label', 'profiles', 'description', 'tags', 'faculty', 'desc']
    inlines = [
        ProjectImagesInline
    ]


class ProfileImagesInline(admin.TabularInline):
    model = ProfileImages

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ProfileImagesInline
    ]

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tags)
admin.site.register(Roles)
admin.site.register(ProfilesToVerify)
admin.site.register(ProjectsToVerify)
admin.site.register(ProjectRoles)
admin.site.register(Faculty)