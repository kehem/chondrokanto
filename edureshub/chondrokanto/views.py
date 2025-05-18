from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
    information = info.objects.get(id=1)
    categorys = category.objects.all()
    context = {
        'info': information,
        'category': categorys,
    }
    return render(request, 'chondro/index.html',context)

def about(request):
    return render(request, 'chondro/about.html')

def my_blog(request):
    information = info.objects.get(id=1)
    my_blog = blog.objects.all()
    full_category = category.objects.all()
    context = {
        'info': information,
        'blog': my_blog,
        'category': full_category,
    }
    return render(request, 'chondro/blog.html',context)


def blogview(request,id):
    information = info.objects.get(id=1)
    full_category = category.objects.all()
    s_blog = blog.objects.get(id=id)
    latest = blog.objects.all().order_by('-published_date')[:5]
    context = {
        'info': information,
        'blog': s_blog,
        'category': full_category,
        'latest': latest,

    }
    return render(request, 'chondro/blogview.html',context)


def my_category(request,id):
    information = info.objects.get(id=1)
    full_category = category.objects.all()
    categorys = category.objects.get(id=id)
    albums = album.objects.filter(category=categorys)
    context = {
        'info': information,
        'cat': categorys,
        'category': full_category,
        'album': albums,
    }
    return render(request, 'chondro/category.html',context)

def videos(request,id):
    information = info.objects.get(id=1)
    full_category = category.objects.all()
    myalbum = album.objects.get(id=id)
    videos = video.objects.filter(album=myalbum)
    context = {
        'info': information,
        'cat': myalbum,
        'category': full_category,
        'video': videos,
    }
    return render(request, 'chondro/videos.html',context)


def dashboard(request):
    return render(request, 'dashboard/index.html')

def information(request):
    data = info.objects.get(id=1)
    instance = info.objects.get(id=1)
    form = infoForm(instance=instance)
    if request.method == 'POST':
        form = infoForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'infoform': form,'title':'dashboard'}
    return render(request, 'dashboard/info.html', context)

def blog_dashboard(request):
    data = blog.objects.all()
    form = blogForm()
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/blog.html', context)


def blog_dashboard_edit(request, id):
    data = blog.objects.all()
    instance = blog.objects.get(id=id)
    form = blogForm(instance=instance)
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/blog.html', context)


def category_dashboard(request):
    data = category.objects.all()
    form = categoryForm()
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/category.html', context)



def category_dashboard_edit(request,id):
    data = category.objects.all()
    instance = category.objects.get(id=id)
    form = categoryForm(instance=instance)
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/category.html', context)


def album_dashboard(request):
    data = album.objects.all()
    form = albumForm()
    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/album.html', context)

def album_dashboard_edit(request,id):
    data = album.objects.all()
    instance = album.objects.get(id=id)
    form = albumForm(instance=instance)
    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/album.html', context)


def video_dashboard(request):
    data = video.objects.all()
    form = videoForm()
    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/video.html', context)

def video_dashboard_edit(request,id):
    data = video.objects.all()
    instance = video.objects.get(id=id)
    form = videoForm(instance=instance)
    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/index.html')
    context = {'form': form,'title':'dashboard','data': data}
    return render(request, 'dashboard/video.html', context)