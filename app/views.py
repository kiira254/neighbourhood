from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserProfileForm, PostForm, CommentForm, BusinessForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import UserProfile, Neighborhood,Business,Location, Comment,Post
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError

# Create your views here.

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to Mini-Insta.',
            f'Hello {name},\n '
            'Welcome to the Nighbourhood.',
            'nkamotho69@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form, 'name': name})

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    try:
        profile = UserProfile.objects.get(user = current_user)
    except:
        return redirect('new_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.neighborhood = profile.neighborhood
            post.type = request.POST['type']
            post.save()

            if post.type == '1':
                recipients = UserProfile.objects.filter(neighborhood=post.neighborhood)
                for recipient in recipients:
                    send_a_email(post.title,post.content,recipient.email)

        return redirect('post')
    else:
        form = PostForm()
    return render(request,'index.html',{"posts":posts,"profile":profile,"form":form})

@login_required(login_url='/accounts/login/')
def new_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        try:
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(request.POST,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
        except:
            form = UserProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
    else:
        if UserProfile.objects.filter(id=1):
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(instance=profile)
        else:
            form = UserProfileForm()
    return render(request,'profile/new_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search(request):
    current_user = request.user
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        business = Business.objects.filter(name__icontains=search_term)
        return render(request,'search.html',{'business':business})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('post',id = post.id)
    else:
        form = CommentForm()
    return render(request,'post.html',{"post":post,"comments":comments,"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    neighborhood = UserProfile.objects.get(user = current_user).neighborhood
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.neighborhood = neighborhood
            business.save()
            return redirect('business')
    else:
        form = BusinessForm()

    try:
        business = Business.objects.filter(neighborhood = neighborhood)
    except:
        business = None

    return render(request,'business.html',{"business":business,"form":form})

class BusinessList(APIView):
    def get(self, request, format=None):
        all_businesses = Business.objects.all()
        serializers = BusinessSerializer(all_businesses, many=True)
        return Response(serializers.data)

    