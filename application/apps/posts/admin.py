from django.contrib import admin

from posts.models import Post, PostLikes


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'created_date')


@admin.register(PostLikes)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_date')
