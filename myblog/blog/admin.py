#coding:utf-8
from django.contrib import admin
#from django.core.urlresolvers import reverse
#from django.utils.html import format_html
from blog import models

class AdminBlogShow(admin.ModelAdmin):

    list_per_page = 5
    list_display = ("title","author","summary","created","status")
    ordering = ['created']

    #修改为发布状态
    def make_published(self,request,queryset):
        rows_updated = queryset.update(status='p')
        self.message_user(request,"已将%s条博客成功发布" % rows_updated)
    make_published.short_description = "将状态更新为已发布"

    #修改为草稿状态
    def make_writing(self,request,queryset):
        rows_updated = queryset.update(status='w')
        self.message_user(request,"已将%s条博客设为草稿" % rows_updated)
    make_writing.short_description = "将状态更新为草稿"

    #根据创建时间和状态过滤分类
    list_filter = ["created","status"]
    #将状态修改功能添加到后台操作上
    actions = [make_published,make_writing]
    #添加搜索功能：搜索标题摘要和正文
    search_fields = ["title","summary","content"]

class AdminCategoryShow(admin.ModelAdmin):

    def published_count(self,obj):
        return obj.published_count()
	
    list_display = ('name','published_count')

class AdminTagShow(admin.ModelAdmin):
	
    def published_count(self,obj):
        return obj.published_count()

    list_display = ('name','published_count')

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
