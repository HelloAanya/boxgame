from django.shortcuts import render

def clock(request):
    return render(request, 'clock.html')




