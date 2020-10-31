from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserProfileForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import Profile
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
            'Welcome to Mini-Insta.',
            'nkamotho69@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('post')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form, 'name': name})

def home(request):

    return render(request, 'index.html')

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
        if UserProfile.objects.filter(user=current_user):
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(instance=profile)
        else:
            form = UserProfileForm()
    return render(request,'profile/new_profile.html',{"form":form})
