from django.contrib import admin
from booknow.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'phone', 'child_name', 'age', 'sex', 'date')