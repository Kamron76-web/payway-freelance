from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Job, FreelancerProfile, Bid
from .forms import RegisterForm, JobForm, BidForm


def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'jobs': jobs})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Login yoki parol xato'

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = JobForm()

    return render(request, 'post_job.html', {'form': form})


@login_required
def profile_view(request):
    profile = FreelancerProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    bids = job.bids.all().order_by('-created_at')
    form = BidForm()

    return render(request, 'job_detail.html', {
        'job': job,
        'bids': bids,
        'form': form
    })


@login_required
def add_bid(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.job = job
            bid.user = request.user
            bid.save()
            return redirect(f'/job/{job.id}/')

    return redirect(f'/job/{job.id}/')
