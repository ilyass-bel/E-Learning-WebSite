from django.forms import ModelForm
from .models import Contenu, Cours, Traveaux, Rendus, Question, Reponse


class ContenuForm(ModelForm):
    class Meta:
        model = Contenu
        fields = '__all__'


class CoursForm(ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'


class TraveauxForm(ModelForm):
    class Meta:
        model = Traveaux
        fields = '__all__'


class RenduForm(ModelForm):
    class Meta:
        model = Rendus
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ReponseForm(ModelForm):
    class Meta:
        model = Reponse
        fields = '__all__'