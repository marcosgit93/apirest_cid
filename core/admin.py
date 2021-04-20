from django.contrib import admin
# Register your models here.
from import_export import resources
from core.models import Cid
from import_export.admin import ImportExportModelAdmin
class BookResource(resources.ModelResource):

    class Meta:
        model = Cid

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Cid,BookAdmin)