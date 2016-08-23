from django.contrib import admin
from blog import models

class AdminBlogShow(admin.ModelAdmin):
    list_display = ("title","author","created")

class AdminCategoryShow(admin.ModelAdmin):
    list_display = ('name',)

class AdminTagShow(admin.ModelAdmin):
    list_display = ('name',)
    
class AdminAboutMe(admin.ModelAdmin):
	list_display = ('title','content')

class AdminFriends(admin.ModelAdmin):
	list_dispaly = ('title','content')

admin.site.register(models.Blog,AdminBlogShow)
admin.site.register(models.Category,AdminCategoryShow)
admin.site.register(models.Tag,AdminTagShow)
admin.site.register(models.Aboutme,AdminAboutMe)
admin.site.register(models.Friends,AdminFriends)
# Register your models here.
