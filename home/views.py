from django.shortcuts import render
from .models import Apropos

# Create your views here.
def accueil(request):
    apropos = Apropos.objects.all()
    context = {
        "apropos": apropos,
    }
    return render(request, 'accueil.html', context)
