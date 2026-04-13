from django.shortcuts import render

from .models import NewsItem, MeetupImage


def home(request):
    meetup_images = MeetupImage.objects.all()
    return render(request, 'pages/home.html', {'meetup_images': meetup_images})


def about(request):
    return render(request, 'pages/about.html')


def news(request):
    items = NewsItem.objects.all()
    return render(request, 'pages/news.html', {'news_items': items})


def venue(request):
    return render(request, 'pages/venue.html')


def speaking(request):
    return render(request, 'pages/speaking.html')
