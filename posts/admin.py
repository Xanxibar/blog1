from django.contrib import admin

from .forms import PostForm
from .models import Comment, Post, Tag


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'text']

admin.site.register(Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'c_count', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    form = PostForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        try:
            tags = ",".join([str(i) for i in obj.tags.all()])
        except:
            tags = None
        if tags:
            form.base_fields['tags'].initial = tags
        form.base_fields['author'].initial = request.user
        return form

    def save_model(self, request, obj, form, change):
        form.author = request.user
        form.save()
        form.create_tags()
        super(PostAdmin, self).save_model(request, obj, form, change)
        

admin.site.register(Post, PostAdmin)


admin.site.register(Tag)