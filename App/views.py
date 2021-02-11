from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import service,Rating,Profile
# from django.contrib.auth.decorators import login_required

from .forms import VotingForm, NewProfileForm
from django.http import JsonResponse
# Create your views here.

def home_page(request):
    all_services = service.objects.all()
    return render(request, 'home.html', {"all_services": all_services})

def view_service(request,id):
    single_service = service.objects.filter(id = id)

    all_ratings = Rating.objects.filter(service = id) 
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.service = id
            rate.save()
        return redirect('single_service',id)
        
    else:
        form = VotingForm() 

    calculate = Rating.objects.filter(service = id)
    usability = []
    design = []
    content = []
    average_usability = 0
    average_design = 0
    average_content = 0

    for x in calculate:
        usability.append(x.usability)
        design.append(x.design)
        content.append(x.content)

        if len(usability)>0 or len(design)>0 or len(content)>0:
            average_usability+= round(sum(usability)/len(usability))
            average_design+= round(sum(design)/len(design))
            average_content+= round(sum(content)/len(content))
        else:
            average_usability = 0.0
            average_design = 0.0
            average_content = 0.0

    return render(request,'service.html',{"single_service":single_service, "all_ratings":all_ratings,"form":form,"usability":average_usability,"design":average_design,"content":average_content})

def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

def my_profile(request):
    current_user = request.user
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"my_profile":my_profile})

def all_users(request):
    users = Profile.objects.all()
    return render(request, 'users.html', {"users":users})

def one_user(request,id):
    user = Profile.objects.filter(id = id)
    return render(request, 'one_user.html', {"user":user})

