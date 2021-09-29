from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from portfolio.models import Project, Testimonial
# Register your models here.


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'project_name')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'project_name')


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'review_name', 'designation')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'review_name', 'designation')
