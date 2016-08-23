# coding=utf8
from django import forms

class CommentForm(forms.Form):

    name = forms.CharField(label='昵称',max_length=16,error_messages={
        'required':'请填写昵称',
        'max_length':'昵称超长'
        })

    email = forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
        })

    content = forms.CharField(label='评论内容',error_messages={
        'required':'请填写您的评论内容',
        'max_length':'评论内容过长'
        })

