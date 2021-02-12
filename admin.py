from django.contrib import admin
from .models import Cours, Contenu, Traveaux, Rendus, Question, Reponse

admin.site.site_header='Educa administration'

admin.site.register(Cours)
admin.site.register(Traveaux)
admin.site.register(Contenu)
admin.site.register(Rendus)
admin.site.register(Question)
admin.site.register(Reponse)