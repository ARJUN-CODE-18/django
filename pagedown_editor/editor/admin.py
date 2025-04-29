# File: pagedown_editor/editor/admin.py

from django.contrib import admin
from .models import TheBookLost

@admin.register(TheBookLost)
class TheBookLostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')
