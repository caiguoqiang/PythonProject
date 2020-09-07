from django.db import models

# Create your models here.


class Article(models.Model):
    # 文章唯一ID（自增）
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    #主要内容
    content=models.TextField()
    # 发布日期,默认为当前日期
    publish_date = models.DateTimeField(auto_now=True)

    #返回标题
    def __str__(self):
        return self.title