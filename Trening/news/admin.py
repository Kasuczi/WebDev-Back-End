from django.contrib import admin
from .models import Post, Comment


# Register your models here.
# @admin.register(Post) <- zamiast admin.site.register(...)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'status', 'published')
    list_filter = ('author', 'status', 'published')
    search_fields = ('title', 'content')
    ordering = ['status', 'published']
    date_hierarchy = 'published'
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post',
                    'content', 'created', 'updated', 'active')
    raw_id_fields = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)