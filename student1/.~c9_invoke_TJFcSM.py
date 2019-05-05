from django.shortcuts import render
import random

def main(request):
    return render(request, 'student1/main.html')
    
    
def random_results(request):
    area = request.GET.get('area')
    places = Place.objecst
    if area == "경상도":
        places = ['감자밭', '고구마밭', '성원집']
        
        place = random.choice(places)
    return render(request, 'student1/random_results.html', {'area': area, 'place': place})


def first(request):
    return render(request, 'student1/first.html')