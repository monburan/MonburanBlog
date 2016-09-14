# coding=utf8
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

STATUS_CHOICES = (
    ('p','已发布'),
    ('w','草稿'),
)

class Category(models.Model):
    
    name = models.CharField('分类',max_length=16)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

class Tag(models.Model):
    
    name = models.CharField('标签',max_length=16)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

class Blog(models.Model):
    
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)

    summary = models.CharField('摘要',max_length=50)
    content = RichTextField('正文')
    created = models.DateTimeField('创建时间',auto_now_add=True)

    status = models.CharField('状态',max_length=1,choices=STATUS_CHOICES)

    category = models.ForeignKey(Category,verbose_name='分类')
	#每篇文章只能有一个分类，一个分类可以有多个文章
    tag = models.ManyToManyField(Tag,verbose_name='标签')
	#每篇文章有多个分类，一个分类里面有多个文章

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

class Aboutme(models.Model):
    
    title = models.CharField('标题',max_length=32)
    content = RichTextField('关于我')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = '关于我'

class Friends(models.Model):

    title = models.CharField('标题',max_length=32)
    content = RichTextField('好友')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '好友'
        verbose_name_plural = '好友'

#admin.site.register([Category,Tag,Blog])
#Create your models here.
