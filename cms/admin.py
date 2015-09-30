from django.contrib import admin

from cms import models
from django.conf import settings


class PlaceholderAdmin(admin.StackedInline):
    model = models.Placeholder
    extra = 0


class PageAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/codemirror.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/mode/xml/xml.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/mode/htmlmixed/htmlmixed.min.js',
            settings.STATIC_URL + 'cms/js/page.js'
        )

        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/codemirror.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/theme/ambiance.min.css',
                settings.STATIC_URL + 'cms/css/page.css'
            )
        }
    inlines = [PlaceholderAdmin]


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.MediaFile)

