from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse
from .models import *
from .forms import TagForm, PostForm
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

# Create your views here.
def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()


    paginator = Paginator(posts, 2)
    page_num = request.GET.get('page', 1)

    page = paginator.get_page(page_num)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'blog\index.html', context=context)

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog\post_detail.html', context={'post': post})
class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True
    # def get(self, request, slug):
    #     tag = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(instance=tag)
    #     return render(request, 'blog/post_update_form.html',
    #     context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/post_update_form.html',
    #     context={'form': bound_form, 'tag': tag})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog\post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog\post_detail.html', context={'post': post})


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog\post_create_form.html'
    raise_exception = True
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog\post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #
    #     return render(request, 'blog\post_create_form.html', context={'form': bound_form})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog\detail_tag.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog\detail_tag.html', context={'tag': tag})

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog\create_tag.html'
    raise_exception = True
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog\create_tag.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #
    #     return render(request, 'blog\create_tag.html', context={'form': bound_form})

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/update_tag_form.html'
    raise_exception = True
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/update_tag_form.html',
    #     context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/update_tag_form.html',
    #     context={'form': bound_form, 'tag': tag})

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog\delete_tag_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog\list_tags.html', context={'tags': tags})
