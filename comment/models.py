from django.db import models
from  django.contrib.auth.models import User
from  article.models import Article
from django.utils import  timezone
# Create your models here.

class Comment(models.Model):
    auther = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='childen'
    )
    class Meta:
        ordering = ['created']
    def __str__(self):
        return  self.content[:20]