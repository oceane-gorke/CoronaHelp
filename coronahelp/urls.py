"""coronahelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='home'),
    path('image/', views.image, name='image'),
    path('getformdata/', views.get_form_data, name='get-form-data'),
    path('getformdataplus/',views.get_form_data_plus,name= 'get-form-data-plus'),
    path('thanks/', views.thanks,name= 'thanks'),
    path('image/identification/',views.get_donne_identification, name='get-donnee-identification'),
    path('thanks2/', views.thanks2,name= 'thanks2'),
    #path('habitants/<int:id>/', views.citoyen_detail),
    #essai de retour vers identification citoyen suite à l'inscription
    #path('image/inscriptionok/', views.inscriptionok, name ='inscriptionok'),
    path('thanks3/', views.thanks3,name= 'thanks3'),
    path('besoincitoyen/', views.besoincitoyen, name='besoincitoyen'),
    path('image/identification/pagecitoyen/', views.pagecitoyen),
    path('image/identification/besoinparticulier/', views.besoinparticulier, name='besoinparticulier'),
    path('accueilcollectivite/', views.get_donne_identification_collectivite, name='get-donnee-identification-collectivite'),
    path('accueilcollectivite/cartefoyer/', views.cartefoyer,name='cartefoyer'),
    path('accueilcollectivite/cartefrequence/', views.cartefrequence,name='cartefrequence'),
    path('accueilcollectivite/produits/', views.produits,name='produits'),
    path('accueilcollectivite/regimes/', views.regimes,name='regimes'),




]
