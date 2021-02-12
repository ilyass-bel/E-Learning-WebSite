from django.http import  HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import utilisateurs_autorises
from.forms import ContenuForm, CoursForm, TraveauxForm, RenduForm, QuestionForm, ReponseForm
from .models import Contenu, Cours, Traveaux, Rendus, Question, Reponse
from .filters import CoursFilter, TraveauFilter, RendusFilter


@login_required(login_url='login')
@utilisateurs_autorises(allowed_roles=['students'])
def etudiant(request):
    contenu = Contenu.objects.all()
    myFilter = CoursFilter(request.GET, queryset=contenu)
    contenu = myFilter.qs
    return render(request,'Cours/etudiant.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def enseignant(request):
    contenu = Contenu.objects.all()
    traveaux = Traveaux.objects.all()
    return render(request,'Cours/enseignant.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def traveaux_prof(request):
    traveaux = Traveaux.objects.all()
    myFilter = TraveauFilter(request.GET, queryset=traveaux)
    traveaux = myFilter.qs
    return render(request,'Cours/traveaux.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def rendus_etudiants(request):
    rendu = Rendus.objects.all()
    myFilter = RendusFilter(request.GET, queryset=rendu)
    rendu = myFilter.qs
    return render(request,'Cours/rendus.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def ajouter_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ajouter_contenu')
    else:
        form = CoursForm()
    return render(request, 'Cours/ajouter_cours.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def ajouter_contenu(request):
    if request.method == "POST":
        form = ContenuForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    else:
        form = ContenuForm()
    return render(request, 'Cours/ajouter_contenu.html', locals())



@utilisateurs_autorises(allowed_roles=['teachers'])
def updateCours(request, pk):
    contenu = Contenu.objects.get(id=pk)
    form = ContenuForm(instance=contenu)
    if request.method == 'POST':
        form = ContenuForm(request.POST, instance=contenu)
        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    return render(request, 'Cours/ajouter_contenu.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def supprimerCours(request, pk):
    contenu = Contenu.objects.get(id=pk)
    if request.method == 'POST':
        contenu.delete()
        return redirect('Enseignant')
    return render(request, 'Cours/supprimer.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def ajouterTraveux(request):
    if request.method == "POST":
        form = TraveauxForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    else:
        form = TraveauxForm()
    return render(request, 'Cours/ajouter_traveaux.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def supprimerTraveux(request, pk):
    traveaux = Traveaux.objects.get(id=pk)
    if request.method == 'POST':
        traveaux.delete()
        return redirect('Enseignant')
    return render(request, 'Cours/supprimerTraveaux.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def updateTraveaux(request, pk):
    traveaux = Traveaux.objects.get(id=pk)
    form = TraveauxForm(instance=traveaux)
    if request.method == 'POST':
        form = TraveauxForm(request.POST, instance=traveaux)
        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    return render(request, 'Cours/ajouter_traveaux.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def ajouter_rendu(request):
    if request.method == "POST":
        form = RenduForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('Etudiant')
    else:
        form = RenduForm()
    return render(request, 'Cours/ajouter_rendu.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def supprimer_rendu(request, pk):
    rendu = Rendus.objects.get(id=pk)
    if request.method == 'POST':
        rendu.delete()
        return redirect('Etudiant')
    return render(request, 'Cours/supprimer_rendu.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def ajouter_Question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Etudiant')
    else:
        form = QuestionForm()
    return render(request, 'Cours/Questions.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def boite_reception(request):
    question = Question.objects.all()
    return render(request,'Cours/boite_reception.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def boite_reponse(request):
    questions = Question.objects.all()
    reponse = Reponse.objects.all()
    return render(request,'Cours/boite_reponse.html', locals())


@utilisateurs_autorises(allowed_roles=['teachers'])
def ajouter_Reponse(request):
    if request.method == "POST":
        form = ReponseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    else:
        form = ReponseForm()
    return render(request, 'Cours/Reponse.html', locals())


@utilisateurs_autorises(allowed_roles=['students'])
def rendu_etu(request):
    rendu = Rendus.objects.filter(nom=request.user)
    return render(request,'Cours/mesrendu.html', locals())