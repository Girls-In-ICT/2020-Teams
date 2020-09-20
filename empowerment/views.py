from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from empowerment.forms import UserForm, ProfileForm, BooksComment
from empowerment.models import UserProfile, LibraryBook, Video, BookComment, VideoComment


def home(request):
    form = UserForm(request.POST)
    # form2 = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    context = {
        'form': form,
        # 'form2': form2
    }
    return render(request, 'index.html', context)


def register(request):
    form = UserForm(request.POST)
    form2 = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        form2 = ProfileForm(request.POST, request.FILES)
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        if form.is_valid() and form2.is_valid():
            save_data = form.save()
            get_id = save_data.id
            save_data2 = form2.save(commit=False)
            instance = save_data2
            instance.user = User.objects.get(id=get_id)
            instance.save()
            user = authenticate(request, username=username, password=password)
            # validating user
            if user is not None:
                # loggingingin
                login(request, user)
                # creating logs
                return redirect('main')
    context = {
        'form': form,
        'form2': form2
    }
    return render(request, 'register_student.html', context)


@login_required(login_url='login')
def mainPage(request):
    return render(request, 'main.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def library(request):
    librarydata = LibraryBook.objects.all()
    form = BooksComment(request.POST)
    if request.method == "POST":
        get_comment = request.POST['comment']
        user = User.objects.get(id=request.user.id)
        # get_user = request.POST['userId']
        get_book = request.POST.get('bookId')
        book = LibraryBook.objects.get(id=get_book)
        save_comment = BookComment(userId=user, bookId=book, comment=get_comment)
        save_comment.save()
    context = {
        "librarydata": librarydata,
        "form": form
    }

    return render(request, 'library.html', context)


def comment(request, libraryId):
    librarydata = LibraryBook.objects.all()
    # get_comment = request.POST['comment']
    # print(get_comment)
    if request.method == "POST":
        # comment = request.POST['comment']
        print("valid")

    context = {
        "librarydata": librarydata,
    }

    return render(request, 'library.html', context)


def video(request):
    videosData = Video.objects.all()
    form = BooksComment(request.POST)
    if request.method == "POST":
        get_comment = request.POST['comment']
        user = User.objects.get(id=request.user.id)
        # get_user = request.POST['userId']
        videoss = request.POST.get('videoId')
        get_video = Video.objects.get(id=videoss)
        save_comment = VideoComment(userId=user, videoId=get_video, comment=get_comment)
        save_comment.save()
    context = {
        "videosData": videosData,
        "form": form
    }

    return render(request, 'vedios.html', context)
