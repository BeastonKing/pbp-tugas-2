from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_home(request):
    context = {
        'nama': 'Bintang Pratama',
        'student_id': '2106751373',
    }

    return render(request, "home.html", context)

def show_bonus(request):
    data_film_watchlist = MyWatchList.objects.all()
    films_watched = 0
    films_not_watched = 0

    for film in data_film_watchlist:
        if film.watched == "Sudah":
            films_watched += 1
        else:
            films_not_watched += 1
            
    context = {
        'nama': 'Bintang Pratama',
        'student_id': '2106751373',
        'films_watched': films_watched,
        'films_not_watched': films_not_watched
    }

    return render(request, "bonus.html", context)

def show_mywatchlist(request):
    data_film_watchlist = MyWatchList.objects.all()
    context = {
        'list_film': data_film_watchlist,
        'nama': 'Bintang Pratama',
        'student_id': '2106751373'
    }

    return render(request, "mywatchlist.html", context)

def show_data_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_data_json(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

