from django.contrib import admin

from .models import NewsItem, MeetupImage


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('date_published', 'title')
    search_fields = ('title', 'content')
    list_filter = ('date_published',)
    date_hierarchy = 'date_published'
    ordering = ('-date_published', '-id')


@admin.register(MeetupImage)
class MeetupImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'alt_text', 'created_at')
    list_editable = ('order',)
    search_fields = ('alt_text',)
    ordering = ('order', '-created_at')
