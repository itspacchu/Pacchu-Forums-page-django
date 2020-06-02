from django.contrib import admin
from .models import Snippet
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

@admin.register(Snippet)
class AdminPriv(ImportExportModelAdmin):
    pass