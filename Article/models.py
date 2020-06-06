from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=1132)
    created_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)
    authors = models.ForeignKey(User,on_delete=models.DO_NOTHING,default='lyj')      #外键关联到其他表,因为后面添加的所以需要设置默认值
    is_deleted = models.BooleanField(default=True)
    readed_num = models.IntegerField(default=0)
    #显示title
    def __str__(self):
        return '<Article标题: %s>' % self.title
