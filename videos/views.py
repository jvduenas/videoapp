from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Category, Vids, Featured, Category, Events
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from videos.forms import UploadForm, FeaturedForm, EventsForm, CategoryForm
from django.contrib.auth.decorators import login_required
from videos.filters import VideoFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

#search bar
def search_videos(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        videos = Vids.objects.filter(caption__contains=searched)

        return render(request,'search.html',{'searched':searched, 'videos':videos })
    else:

        return render(request,'search.html',{})


# this is the explore page with pagination 
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse("admin-page"))
    #video=Vids.objects.all()
    #myFilter=VideoFilter(request.GET, queryset=video) 
    #video=myFilter.qs

    paginator = Paginator(Vids.objects.all().order_by('-id'), 6)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={'objects': objects}
    return render(request,'explore.html',context)

@login_required(redirect_field_name='login')
def admin(request):
    video=Vids.objects.all()
    myFilter=VideoFilter(request.GET, queryset=video)
    video=myFilter.qs

    paginator = Paginator(Vids.objects.all().order_by('-id'), 6)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={'video':video, 'myFilter':myFilter, 'objects': objects}

    return render(request,'explore_admin.html',context)

#view individual video using id
def view_video(request, pk):
	video = Vids.objects.get(id=pk)
	return render(request, "view.html", {"video":video})

#home page with featured video
def home_video(request):
    home=Featured.objects.all()
    return render(request, "featured.html",{"home":home})
    

#login page / Authentication
def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse("admin-page"))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('admin-page'))
        else:
            messages.info(request, 'Username OR password is incorrect')
    template = 'login.html'
    return render(request, template)

#logout user
def logout_user(request):
	logout(request)
	return redirect('explore')

# upload new video
@login_required(redirect_field_name='login')
def upload(request):
	form = UploadForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return redirect('admin-page')
	context = {
		'form': form
	}
	return render(request, 'upload.html', context)

# update a video 
@login_required(redirect_field_name='login')
def update_video(request, pk):
    video=Vids.objects.get(id=pk)
    form = UploadForm(instance=video)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('admin-page')
    context = {
        'form':form
    }
    return render(request, 'update.html', context)


#playlist
def video_playlist(request):
    video=Vids.objects.all()
    paginator = Paginator(Vids.objects.all().order_by('-playlist'), 6)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={'objects': objects, 'video':video }
    return render(request,'playlist.html', context)

#delete video
@login_required(redirect_field_name='login')
def delete_video(request, pk):
	video = Vids.objects.get(id=pk)
	if request.method =="POST":
		video.delete()
		return redirect('admin-page')
	context = {}
	return render(request, 'delete.html', {})


#change featured video
@login_required(redirect_field_name='login')
def change_featured(request):
    video=Featured.objects.all()
    if request.method=='POST':
        video.delete()
    form=FeaturedForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('featured')
    context={
        'form':form
    }
    return render(request, 'change_featured.html', context)


#create category/playlist
def create_playlist(request):
    playlist=Category.objects.all()
    form=CategoryForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('category')
    context={
        'form':form,
        'playlist':playlist
    }
    return render(request, 'create_playlist.html', context)



#This is an inactive function and template (will activate in the future)
def category(request):
    video=Category.objects.all()
    return render(request, 'category.html', {'video':video})


#events page

def events(request):
    event=Events.objects.all()
    paginator = Paginator(event.order_by('-id'), 1)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={
        'event':event,
        'objects':objects
    }
    return render(request, 'events.html', context)

@login_required(redirect_field_name='login')
def add_event(request):
    event=Events.objects.all()
    form=EventsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('admin-page')
    context={
        'form':form,
        'event':event
        }
    return render(request, 'addevent.html', context)

#This is as of May 12, 2022




