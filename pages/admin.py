from django.contrib import admin

from .models import NewsItem


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('date_published', 'title')
    search_fields = ('title', 'content')
    list_filter = ('date_published',)
    date_hierarchy = 'date_published'
    ordering = ('-date_published', '-id')
