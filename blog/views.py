from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
# Create your views here.


def ArticleListView(request):
    templateName = 'articles/article_list.html'
    queryset = Article.objects.all()
    context = {'object_list': queryset}
    return render(request, templateName, context)


def ArticleDetailView(request, my_id):
    obj = Article.objects.get(id=my_id)
    context = {'object': obj}
    return render(request, "articles/article_detail.html", context)


def ArticleCreateView(request):
    my_form = ArticleForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ArticleForm()
        return redirect('/articles/')

    context = {'form': my_form}
    return render(request, "articles/article_create.html", context)
