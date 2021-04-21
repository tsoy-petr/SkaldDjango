from django.contrib import admin

from api.models import *

# admin.site.register(Good)
@admin.register(Good)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'isGroup', 'uuid_part', 'uuid', 'id_uuid')
    list_filter = ('name', 'isGroup', 'uuid_part', 'uuid')


admin.site.register(ImageGood)
