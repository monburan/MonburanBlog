# coding=utf8
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Category(models.Model):
    
    name = models.CharField('名称',max_length=16)

class Tag(models.Model):
	
    name = models.CharField('名称',max_length=16)

class Blog(models.Model):
	
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    content = RichTextField('正文')
    created = models.DateTimeField('创建时间',auto_now_add=True)

    category = models.ForeignKey(Category,verbose_name='分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
	
class Comment(models.Model):

    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('昵称',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=140)

    created = models.DateTimeField('创建时间',auto_now_add=True)

class Aboutme(models.Model):
	
	title = models.CharField('标题',max_length=32)
	content = RichTextField('About me')

class Friends(models.Model):

	title = models.CharField('标题',max_length=32)
	content = RichTextField('友情链接')

#admin.site.register([Category,Tag,Blog])
# Create your models here.
