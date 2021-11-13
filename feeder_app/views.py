from django.http.response import HttpResponse
from django.shortcuts import render
from .models import FeederSet
from django.core.cache import cache

def index(request):
    feederSets = []
    if cache.keys('*'):
        for i in cache.keys('*'):
            item = cache.get(i)
            feederSets.append(item)
        print('Cached data: ', feederSets)
    else:
        feederSets = FeederSet.objects.all()

        for i in FeederSet.objects.all():
            cache.set(i.id, i)
        print('Hello from DB. Data are cached')

    context = {'feederSets':feederSets}
    return render(request, 'index.html', context)


def details(request, pk):
    set_id = pk
    if cache.get(set_id):
        set = cache.get(set_id)
        print('hello from cache')
    else:
        try:
            set = FeederSet.objects.get(id=pk)
            cache.set(set_id, set)
            print('hello from db')
            print('cached: ', set_id)
        except FeederSet.DoesNotExist:
            return HttpResponse("this feederSet does not exist")

    context = {"set":set}
    return render(request, 'details.html', context)


