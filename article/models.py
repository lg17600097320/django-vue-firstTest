from django.db import models
from  django.utils import  timezone
from  django.contrib.auth.models import User
from  markdown import  Markdown
# Create your models here.

# 标签
class Tag(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return  self.title

# 文章分类
class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return  self.title

# 图片
class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=100,verbose_name='标题')
    # 正文
    content = models.TextField(verbose_name='内容')
    # 创建时间
    created =  models.DateTimeField(default=timezone.now)
    #更新时间   auto_now=True 调用save方法 自动更新当前时间
    updated = models.DateTimeField(auto_now=True)
    # 作者
    auther = models.ForeignKey(User,null=True,on_delete= models.CASCADE,related_name='articles')
    # 分类
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.SET_NULL,related_name='articles')
    # 标签
    tag = models.ManyToManyField(Tag,blank=True,related_name='articles')
    # 图片
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc'
            ]
        )
        md_content = md.convert(self.content)
        # md.toc 是渲染后的目录
        return  md_content,md.toc
    class Meta:
        ordering= ['-created']
    def __str__(self):
        return self.title

