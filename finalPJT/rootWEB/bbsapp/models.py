from django.db import models
# 추가
from django.utils import timezone

# Create your models here.
class BbsUser(models.Model):
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id+"\t"+self.user_pwd+'\t'+self.user_name


# sql lite 자동으로 id 컬럼의 primary key생성해준다
class Bbs(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField(default=timezone.now())
    viewcnt = models.IntegerField(default=0)