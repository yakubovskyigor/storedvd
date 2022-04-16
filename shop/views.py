from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Photo, Article, Single


def index(request):
    photos = Photo.objects.all().order_by()[:10]
    context = {'photos': photos}
    return render(
        request,
        'index.html',
        context=context
    )


# def get_order_by_photos(request):
#     order_by = ''
#     if request.GET.__contains__('sort') and request.GET.__contains__('up'):
#         sort = request.GET['sort']
#         up = request.GET['up']
#         if sort == 'title':
#             if up == '0':
#                 order_by = '-'
#             order_by += sort
#         print(order_by)
#
#     return 'title'


def about(request):
    return render(
        request,
        'about.html',
    )


def contacts(request):
    return render(
        request,
        'contacts.html',
    )


def blog(request):
    # obj = Article.objects.get(pk=id)
    # obj = get_object_or_404(Article, pk=id)
    # photos = Photo.objects.filter(blog_exact=obj).order_by()
    # context = {'blog': obj, 'photos': photos}
    return render(
        request,
        'blog.html'
    )


def single(request):
    return render(
        request,
        'single.html',
    )


# class SingleDetailView(generic.DetailView):
#     model = Single

