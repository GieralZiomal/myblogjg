from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import articles

# Create your views here.
def mainpage(request):
    return render(request, 'index.html')

def blog(request):
    mydata = articles.objects.all().values()
    context = {
    'articleslist': mydata,
    }
    return render(request, 'blog.html', context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(articles, id=id)
    context =  {
        "object": obj
    }
    return render(request, "article.html", context)