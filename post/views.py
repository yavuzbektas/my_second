from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def post_index(request):
    posts_list = Post.objects.all()
    query=request.GET.get('q')
    if query:
        posts_list=posts_list.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query) |
                                     Q(user__first_name__icontains=query) |
                                     Q(user__last_name__icontains=query)
                                     ).distinct()
    paginator = Paginator(posts_list, 3)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)


    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {

        'post': post,
        'form': form,

    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        raise Http404('Yetkili Kullanıcı değilsiniz')
    # if request.method=="POST":
    #     #formdan gelen bilgeri kaydeder
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # else:
    #     # Formu Kullanıvıya göster
    #     form = PostForm()

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'başarılı bir şekilde olusturdunuz', extra_tags='mesaj_basarili')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }

    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        raise Http404('Yetkili Kullanıcı değilsiniz')
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()

        messages.success(request, 'basarılı bir sekilde olusturdunuz', extra_tags='mesaj basarılı')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        raise Http404('Yetkili Kullanıcı değilsiniz')
    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('post:index')
