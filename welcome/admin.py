from django.contrib import admin

from .models import PageView, Book

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
admin.site.register(Book)
