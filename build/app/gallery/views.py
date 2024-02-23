from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request, 'gallery/map.html')

def viewer(request, view_name):
    return render(request, f'gallery/{view_name}.html')