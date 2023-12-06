from django.contrib import admin
from . models import Partenaires, Avis, Galerie, Apropos

# Register your models here.
admin.site.register(Partenaires)
admin.site.register(Avis)
admin.site.register(Galerie)
admin.site.register(Apropos)