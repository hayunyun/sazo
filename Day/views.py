from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip


def modeling(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        description = request.POST.get('description')
        price = request.POST.get('price')
        time = request.POST.get('time')
        photo = request.POST.get('photo')
        trip = Trip(name=name, address=address, description=description, price=price, time=time, photo=photo)
        trip.save()
        return redirect('list')
    return render(request, 'Day/modeling.html')
    
    
def list(request):
    trips = Trip.objects.all()
    return render(request, 'Day/list.html', {'trips' : trips})