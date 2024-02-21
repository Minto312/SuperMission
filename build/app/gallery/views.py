from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request, 'gallery/map.html')

def viewer(request):
    return render(request, 'gallery/viewer.html')