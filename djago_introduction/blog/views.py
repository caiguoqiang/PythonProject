from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
# Create your views here.
def hello_world(request):
    return HttpResponse("helloworld")


def Article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    article_content = article.brief_content
    content = article.content
    publish_date = article.publish_date.date()

    return_str = 'title:%s, articel_content:%s,content:%s,publish_date:%s'\
                 %(title,article_content,content,publish_date)
    return HttpResponse(return_str)

def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    #print('page parmar',page)
    all_artcle = Article.objects.all()
    top5_artcle_list = Article.objects.order_by('publish_date')[:4]
    paginator = Paginator(all_artcle,5)
    page_num = paginator.num_pages
    #print('page num',page_num)
    page_artcle_list = paginator.page(page)
    if page_artcle_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_artcle_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page

    return render(request,'blog/index.html',
                  {
                      'artcle_list':page_artcle_list,
                      'page_num':range(1,page_num+1),
                      'curr_page':page,
                      'next_page':next_page,
                      'previous_page':previous_page,
                      'top5_artcle_list':top5_artcle_list,
                  }
                  )

def get_detail_page(request,artcle_id):
    all_artcle = Article.objects.all()
    #print(type(all_artcle))
    curr_artcle = None
    previous_index = 0
    next_index = 0
    previous_artcle = None
    next_artcle = None
    for index,artcle in enumerate(all_artcle):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_artcle)-1:
            previous_index= index -1
            next_index = index
        else:
            previous_index = index + 1
            next_index = index - 1
        if artcle.article_id == artcle_id:
            curr_artcle = artcle
            previous_artcle = all_artcle[previous_index]
            next_artcle = all_artcle[next_index]
            break

    #curr_artcle = Article.objects.all()[0]
    section_list = curr_artcle.content.split('\n')
    return render(request,'blog/detail.html',
                  {
                      'curr_artcle':curr_artcle,
                      'section_list':section_list,
                      'previous_artcle':previous_artcle,
                      'next_artcle':next_artcle,

                  }
                  )