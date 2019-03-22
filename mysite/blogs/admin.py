from django.contrib import admin
from . models import Blog

#modified Customized Admin Option
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_display_links = ["title", "date"]
    list_filter = ["date"]
    class Meta:
        model = Blog

admin.site.register(Blog, PostModelAdmin)


