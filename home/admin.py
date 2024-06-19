from django.contrib import admin
from . models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'short_description')
admin.site.register(Product ,ProductAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
admin.site.register(News, NewsAdmin)