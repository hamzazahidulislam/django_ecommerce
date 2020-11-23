from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def user_profile(request):
    # user = request.user
    # profile = Profile.objects.get(user=user)
    # profile = user.profile
    # context = {'profile': profile, 'user': user}

    Profile.objects.get_or_create(user=request.user)
    return render(request, 'account/profile.htm')


    # return render(request, 'account/profile.htm')


@login_required
def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user-dashboard')

    context = {'form': form}
    return render(request, 'account/create_profile.htm', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'account/edit_profile.htm', context)


@login_required
def create_post(request):
    form = CreatePost()
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form
    }
    return render(request, 'account/create-post.htm', context)


@login_required
def user_dashboard(request):
    return render(request, 'dashboard/dashboard/dashboard.html')


def user_signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponseRedirect(reverse('user-login'))

    context = {
        'form': form
    }
    return render(request, 'account/register.htm', context)


def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    context = {
        'form': form,
    }
    return render(request, 'account/login.htm', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user-login'))