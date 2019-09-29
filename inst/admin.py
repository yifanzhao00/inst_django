from django.contrib import admin

from inst.models import Post, InstUser, Like, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(InstUser)
admin.site.register(Like)
admin.site.register(UserConnection)
