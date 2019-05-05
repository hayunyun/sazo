from django.shortcuts import render,redirect
import random
from Day.models import Trip

def main(request):
    return render(request, 'student1/main.html')
    
    
def random_results(request):
    region = request.GET.get('region')
    
    if region == "경상도":
        places = ['감자밭', '고구마밭', '성원집']
        
        
        place = random.choice(places)
    return render(request, 'student1/random_results.html', {'region': region, 'place': place})


def first(request):
    region = request.GET.get('region')
    sample_places = Trip.objects.filter(region=region)
    random_place = random.choice(sample_places)
    context = {
        'random_place':random_place,
        'sample_places': sample_places,
    }
            
    return render(request, 'student1/first.html', context)