from django.contrib import admin

from hello.models import Person, Category, Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'img')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('date',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'photo')
    list_display_links = ('id', 'name')

admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)