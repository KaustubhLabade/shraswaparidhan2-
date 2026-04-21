from django.contrib import admin
from .models import Category, Dress

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'dress_count']
    list_filter = ['parent']
    search_fields = ['name']

    def dress_count(self, obj):
        return obj.dresses.count()
    dress_count.short_description = 'Costumes'

@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'available']
    list_filter = ['category', 'available']
    search_fields = ['name']
    list_editable = ['available']

admin.site.site_header = 'Shraswa Paridhan Admin'
admin.site.site_title = 'Shraswa Paridhan'
admin.site.index_title = 'Costume & Category Management'
