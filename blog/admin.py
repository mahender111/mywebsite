from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','author','publish','status')
    list_filter = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
