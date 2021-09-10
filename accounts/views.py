
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import Anime, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse
from django.db.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.



def dashboard(request):
    anime = Anime.objects.all()[:3]
    context = {'anime' : anime}
    return render(request, 'accounts/dashboard.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.success(request, 'Both Username and Password are required')
            return redirect('/login')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not Found')
            return redirect('/login')
           
        user = authenticate(username=username, password=password)

        if user is None:
            messages.success(request, 'Wrong Password')
            return redirect('/login')

        login(request, user)
        return redirect('/home')



    return render(request, 'accounts/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/login')

def register(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=username).first():
            messages.success(request, 'Username is taken.')
            return redirect('/register')
        if User.objects.filter(email=email).first():
            messages.success(request, 'Email is taken.')
            return redirect('/register')
        

        user_obj = User(username=username, email=email, first_name = fname, last_name=lname)
        user_obj.set_password(password)
        user_obj.save()

        profile_obj = Profile.objects.create(user = user_obj)
        profile_obj.save()
        messages.success(request, 'Account created for ' + username)
        return redirect('/login')

    return render(request, 'accounts/register.html')

@login_required(login_url='/login')
def homepage(request):
    anime = Anime.objects.all()[:8]
    animes = Anime.objects.all()



    # ratings = []
    # for i in anime:
    #     anime_rate = Anime.objects.get(id= i.id)

    #     reviews = Reviews.objects.filter(anime=anime_rate)

    #     ratings.append( reviews.aggregate(Avg('rate')))

        
 


    



    context = {'animes' : anime , 'ani' : animes, }

    return render(request, 'accounts/homepage.html', context)





@login_required(login_url='/login')
def profile(request):
    
    username = request.user.username
    user = User.objects.filter(username=username).first()

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email_ = request.POST.get('email')

        User.objects.filter(first_name=user.first_name).update(first_name=fname)
        User.objects.filter(last_name=user.last_name).update(last_name=lname)
        User.objects.filter(email=user.email).update(email=email_)

        return redirect('/profile')
    

    review = Reviews.objects.all()



    context = {'review' : review}
    return render(request, 'accounts/profile.html', context)



@login_required(login_url='/login')
def feed(request):
    animes = Anime.objects.all()



    return render(request, 'accounts/review-feed.html', {'animes' : animes })



@login_required(login_url='/login')
def Rate(request, anime_id):
    user = request.user
    anime = Anime.objects.get(id=anime_id)
    reviews = Reviews.objects.filter(anime=anime)
    review_avg = reviews.aggregate(Avg('rate'))
    review_count = reviews.count()

    form = RateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.anime = anime
            rate.save()
        else:
            form = RateForm()
    context = {'form' : form, 'animes' : anime,  'reviews' : reviews, 'review_avg' : review_avg, 'review_count' : review_count, }
    return render(request, 'accounts/review.html', context)

def searchBar(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        anime = Anime.objects.filter(anime_name__contains = searched)

        return render(request, 'accounts/search.html', {'searched': searched, 'animes':anime})
        
    else:
        return render(request, 'accounts/search.html', {})





    

    