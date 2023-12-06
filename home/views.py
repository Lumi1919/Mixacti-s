from django.shortcuts import render

# Create your views here.
def accueil(request):
    context = {}
    return render(request, 'accueil.html', context)
