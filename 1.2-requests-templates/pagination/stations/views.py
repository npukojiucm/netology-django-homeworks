import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


with open(f'{settings.BUS_STATION_CSV}', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    bus_station = []

    for row in reader:
        bus_station.append(row)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_station, 10)
    page = paginator.get_page(page_number)

    context = {
        # 'bus_stations': bus_station,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
