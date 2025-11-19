from django.contrib import admin

from snippets.models import Snippet, Tag

admin.site.register(Snippet)
admin.site.register(Tag)