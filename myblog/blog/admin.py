#coding:utf-8
from django.contrib import admin
from blog import models

class AdminBlogShow(admin.ModelAdmin):
    list_display = ("title","author","summary","created","status")
    ordering = ['title']
    def make_published(self,request,queryset):
        rows_updated = queryset.update(status='p')
        self.message_user(request,"已将%s条博客成功发布" % rows_updated)
    make_published.short_description = "将状态更新状态为已发布"
    def make_writing(self,request,queryset):
        rows_updated = queryset.update(status='w')
        self.message_user(request,"已将%s条博客设为草稿" % rows_updated)
    make_writing.short_description = "将状态更新为草稿"
    actions = [make_published,make_writing]
#    fieldsets = [
#        ('标题',{'fields':['title']}),
#        ('作者',{'fields':['author']}),
#	]
class AdminCategoryShow(admin.ModelAdmin):
    list_display = ('name',)

class AdminTagShow(admin.ModelAdmin):
    list_display = ('name',)
    
class AdminAboutMe(admin.ModelAdmin):
    list_display = ('title',)

class AdminFriends(admin.ModelAdmin):
    list_dispaly = ('title',)

admin.site.register(models.Blog,AdminBlogShow)
admin.site.register(models.Category,AdminCategoryShow)
admin.site.register(models.Tag,AdminTagShow)
admin.site.register(models.Aboutme,AdminAboutMe)
admin.site.register(models.Friends,AdminFriends)
# Register your models here.
