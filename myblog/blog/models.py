# coding=utf8
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Category(models.Model):
    
    name = models.CharField('名称',max_length=16)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
	
    name = models.CharField('名称',max_length=16)

    def __unicode__(self):
		return self.name
		
class Blog(models.Model):
	
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    content = RichTextField('正文')
    created = models.DateTimeField('创建时间',auto_now_add=True)

    category = models.ForeignKey(Category,verbose_name='分类')#每篇文章只能有一个分类，一个分类可以有多个文章
    tag = models.ManyToManyField(Tag,verbose_name='标签')#每篇文章有多个分类，一个分类里面有多个文章

class Aboutme(models.Model):
	
	title = models.CharField('标题',max_length=32)
	content = RichTextField('About me')

class Friends(models.Model):

	title = models.CharField('标题',max_length=32)
	content = RichTextField('友情链接')

#admin.site.register([Category,Tag,Blog])
# Create your models here.
