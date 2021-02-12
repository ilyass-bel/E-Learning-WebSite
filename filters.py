import django_filters
from .models import *


class CoursFilter(django_filters.FilterSet):
    class Meta:
        model = Contenu
        fields = ['cours']


class TraveauFilter(django_filters.FilterSet):
    class Meta:
        model = Traveaux
        fields = ['semestre', 'filiere']


class RendusFilter(django_filters.FilterSet):
    class Meta:
        model = Rendus
        fields = ['semestre', 'filiere']