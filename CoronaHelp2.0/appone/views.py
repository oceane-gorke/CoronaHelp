from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.urls import reverse

from appone.forms import Foyer
from appone.forms import Habitant
from appone.forms2 import Identification
from appone.forms2 import IndentificationForm
from appone.models import Habitant as ModelHabitant
from appone.forms import Produit
#from appone.forms import NBProduit
from appone.forms2 import IdentificationC
from appone.forms2 import IndentificationFormC
from appone.models import Collectivite as ModelCollectivite
from django.forms import formset_factory

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import io
import matplotlib.pyplot as plt; plt.rcdefaults()

from django.template import loader #pour charger les templates


# Create your views here.

def accueil(request):
    template = loader.get_template('appone/accueil.html')
    context = {
        'images': [
            {
                'nom': 'Coronavirus',
                'nom_fichier': '98061289_234100281356065_6674102895622750208_n.png'
            }
        ]

    }
    return HttpResponse(template.render(context, request))

def thanks(request):
    return HttpResponse('Merci ! Votre foyer a été enregistré avec succes! ')


def get_form_data_plus(request):
    if request.method == 'POST':
        form=Habitant(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            return HttpResponse('Ouups... Vos informations saisies ne sont pas valides. Veuillez réessayer.')
    else:
        form2 = Habitant()
        return render(request, 'appone/form2.html', {'form': form2})



def get_form_data(request):
    if request.method == 'POST':
        print("In POST processing")
        form = Foyer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get-form-data-plus')
    else:
        form =Foyer()
    return render(request, 'appone/form.html', {'form': form})

def thanks2(request):
        return HttpResponse("Authentification en cours... Veuillez patienter...<br/><br/>Désolé, l'identifiant ou le mot de passe est incorrect."
                            "<br/><br/>Veuillez réessayer.")

def thanks3(request):
    return HttpResponse('Identification réussie. Bienvenue')

def image(request): #pour afficher l'image
    template=loader.get_template('appone/form3.html')
    context = {
        'images': [
            {
                'nom':'Prevention Coronavirus',
                'nom_fichier': 'Coronavirus.png'
            }
        ]

    }
    return HttpResponse(template.render(context,request))

def get_donne_identification(request):
    if request.method == 'POST': #le formulaire a été posté
        print('Traitement des données en cours')
        form = IndentificationForm(request.POST) #on recupere les valeurs posté dans le formulaire
        if form.is_valid():
            print('email:', form.cleaned_data['email']) #on affiche la donnée saisie dans le formulaire
            print('mdp:', form.cleaned_data['mdp'])
            if ModelHabitant.objects.get(email=form.cleaned_data['email']) is not None:
                print('Vérification en cours...')
                #return HttpResponseRedirect(reverse('thanks3'))
                return render(request, 'appone/besoincitoyen.html')
            else:
                return HttpResponseRedirect(reverse('thanks2'))
    else: #on fait un GET, on veut juste afficher le formulaire dans le navigateur
        form= Identification()
    return render(request, 'appone/identification.html', {'form': form})


def pagecitoyen(request):
    #ArticleFormSet=formset_factory(Produit, extra=2, min_num=1, validate_min=True)
    form=Produit(request.POST)
    if request.method == 'POST':
        #formset = ArticleFormSet(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(
                "<h2>Merci, votre demande sera traitée dans les plus brefs délais. <br>Si vous désirez d'autres produits, veuillez faire retour et retournez à la page de saisie des produits. <br> <br>En attendant, continuez à vous protéger et à appliquer les gestes barrières. </h2>")

            #return HttpResponseRedirect(reverse('thanks4'))
            #nb_produits = int(form.cleaned_data['nb_produits'])
            # for i in range (nb_produits):
            #     return redirect('')
    else:
        form=Produit()
        #formset=ArticleFormSet()
    return render(request, 'appone/pagecitoyen.html', {'form': form})

def besoinparticulier(request):
    return render(request, 'appone/besoinparticulier.html')


#def inscriptionok(request):
  #  return render(request, 'appone/inscriptionok.html')

def besoincitoyen(request):
    return render(request, 'appone/besoincitoyen.html')

def citoyen_detail(request, id):
    try:
        hab=ModelHabitant.objects.get(id=id)
    except ModelHabitant.DoesNotExist:
        return HttpResponse(status=404)
    return HttpResponse(hab)

def get_donne_identification_collectivite(request):
    if request.method == 'POST': #le formulaire a été posté
        print('Traitement des données en cours')
        form = IndentificationFormC(request.POST) #on recupere les valeurs posté dans le formulaire
        if form.is_valid():
            print('id:', form.cleaned_data['id']) #on affiche la donnée saisie dans le formulaire
            print('mdp:', form.cleaned_data['mdp'])
            if ModelCollectivite.objects.get(id=form.cleaned_data['id']) is not None:
                print('Vérification en cours...')
                #return HttpResponseRedirect(reverse('thanks3'))
                return HttpResponse('Ok')
            else:
                return HttpResponse('Ok')
    else: #on fait un GET, on veut juste afficher le formulaire dans le navigateur
        form= IdentificationC()
    return render(request, 'appone/accueilcollectivite.html', {'form': form})

def menuvisuel(request):
    return render(request, 'appone/menuvisuel.html')


def cartefoyer(request):
    fig = Figure()
    canvas = FigureCanvas(fig)
    x, y = np.loadtxt('/Users/gorkeoceane/CoronaHelp2.0/appone/dataset.csv', delimiter=',', unpack=True, encoding="utf8")
    plt.bar(x, y, align='center', alpha=0.5, label="Nombre d'habitants par foyers")
    plt.ylabel('Nombre de foyers')
    plt.xlabel("Nombre d'habitants")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    plt.close(fig)
    return response

def cartefrequence(request):
    fig2 = Figure()
    canvas = FigureCanvas(fig2)
    x2, y2 = np.loadtxt('/Users/gorkeoceane/CoronaHelp2.0/appone/dataset2.csv', delimiter=',', unpack=True, encoding="utf8")
    plt.bar(x2, y2, align='center', alpha=0.5, label="Nombre de connexions par jour")
    plt.ylabel('Nombre de connexions')
    plt.xlabel("Jours depuis le 17 mars")
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    response2 = HttpResponse(buf2.getvalue(), content_type='image/png')
    plt.close(fig2)
    return response2

def produits(request):
    #labels = 'poulet','eau','Légumes','fruits','viande','autres'
    fig3 = Figure()
    canvas = FigureCanvas(fig3)
    y3 = np.loadtxt('/Users/gorkeoceane/CoronaHelp2.0/appone/dataset3.csv', unpack=True ,encoding="utf8")
    x3=np.arange(6)
    plt.bar(x3,y3, align='center', alpha=0.5, label="Répartition des produits commandés")
    plt.ylabel('Nombre de commandes en pourcentage')
    plt.xticks(x3,('poulet', 'eau', 'Légumes', 'fruits', 'viande', 'autres'))
    plt.xlabel("Produits")
    buf3 = io.BytesIO()
    plt.savefig(buf3, format='png')
    response3 = HttpResponse(buf3.getvalue(), content_type='image/png')
    plt.close(fig3)
    return response3

def regimes(request):
    fig4 = Figure()
    canvas = FigureCanvas(fig4)
    y4 = np.loadtxt('/Users/gorkeoceane/CoronaHelp2.0/appone/dataset4.csv', unpack=True, encoding="utf8")
    x4 = np.arange(6)
    plt.bar(x4, y4, align='center', alpha=0.5, label="Répartition des produits commandés")
    plt.ylabel('Nombre de demandes en pourcentage')
    plt.xticks(x4, ('non specifique', 'halal', 'casher', 'végétarien', 'sans gluten', 'sans lactose'))
    plt.xlabel("régimes")
    buf4 = io.BytesIO()
    plt.savefig(buf4, format='png')
    response4 = HttpResponse(buf4.getvalue(), content_type='image/png')
    plt.close(fig4)
    return response4