from django.contrib import admin
from .models import *


class CommentInline(admin.StackedInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
