from django.contrib import admin

from .models import Student, University


class StudentInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Student


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    fields = ['name', 'built']
    inlines = [StudentInlineModelAdmin]
