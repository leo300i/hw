from django.contrib import admin
from .models import News, NewsComment, Tag


class CommentInline(admin.StackedInline):
    model = NewsComment
    extra = 5


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = 'id title text created_at updated_at'.split()
    search_fields = 'title text'.split()
    list_filter = 'created_at tags'.split()
    inlines = [CommentInline]


admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment)
admin.site.register(Tag)
