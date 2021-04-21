from django.contrib import admin

from api.models import *

# admin.site.register(Good)
@admin.register(Good)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'isGroup')


admin.site.register(ImageGood)
