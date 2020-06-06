from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import  HttpResponse, Http404
from .models import Article
# Create your views here.

def article_detail(request, article_id):
    article= get_object_or_404(Article,id=article_id)
    context={}
    context['article_obj']=article
    return render_to_response('article_detail.html', context)
    # try:
    #     article = Article.objects.get(id=article_id)
    #     context={}
    #     context['article_obj']=article
    #     #return render(request, 'article_detail.html', context)
    #     return render_to_response('article_detail.html', context)
    # except Article.DoesNotExist:
    #     raise Http404('404')
    # #return HttpResponse("id:%s" %article_id)
    # #return HttpResponse("<h1>标题:%s</h1>,<br> 文章内容%s" %(article.title, article.content))


