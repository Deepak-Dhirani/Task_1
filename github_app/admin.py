from django.contrib import admin
from .models import Repository

@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_private', 'owner')
    search_fields = ('name', 'description', 'owner')
    list_filter = ('is_private',)