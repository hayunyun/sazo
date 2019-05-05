from django.shortcuts import render


def main(request):
    return render(request, 'student1/main.html')
