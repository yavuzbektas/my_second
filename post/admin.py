from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date','slug']
    list_display_links = [ 'content', 'pub_date']
    list_filter = ['title', 'content', 'pub_date']
    search_fields = ['title', 'content']
    list_editable = ['title',]
    # prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model: Post


admin.site.register(Post, PostAdmin)
