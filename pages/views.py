from django.shortcuts import render

from teams.models import Team


def home_page(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def services_page(request):
    return render(request, 'pages/services.html')


def contact_page(request):
    return render(request, 'pages/contact.html')
