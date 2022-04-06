from django.contrib import admin


class WebClipAdminHelper(admin.ModelAdmin):
    search_fields = (
        'page_url',
        'page_title',
    )
    list_display = (
        '__str__',
        'page_url',
    )
    fields = ('page_url', 'page_title', 'html_content')
