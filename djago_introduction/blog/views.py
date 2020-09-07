from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def hello_world(request):
    return HttpResponse("helloworld")

#���ز���������Ϣ
def Article_content(request):
    #չʾ��һƪ����������
    article = Article.objects.all()[0]
    title = article.title
    article_content = article.brief_content
    content = article.content
    publish_date = article.publish_date.date()

    return_str = 'title:%s, articel_content:%s,content:%s,publish_date:%s'\
                 %(title,article_content,content,publish_date)
    return HttpResponse(return_str)
