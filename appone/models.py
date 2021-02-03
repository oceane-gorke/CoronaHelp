from django.db import models

# Create your models here.

CHOIX_TYPE =(
    ('maison', 'Maison'),
    ('appartement','Appartement')
)
CHOIX_RUE = (

    ('rue de la Blanche ', ' De la Blanche'),
    ('rue des Ulysses',' Des Ulysses' ),
    ('rue de la Gare', 'De la Gare'),
    ('rue Jean Mermoz','Jean Mermoz'),
    ('rue Pont de Clé', 'Pont de Clé'),
    ('rue Aristide Brillant','Aristide Brillant')
)
CHOIX_NB_HABITANT = (
    ('1','1 (i.e vous)'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15')
)
CHOIX_REGIME = (

    ('aucun','Aucun'),
    ('vegetarien','Vegetarien'),
    ('vegetalien','Vegetalien'),
    ('vegan','Vegan'),
    ('halal','Halal'),
    ('cacher','Cacher')
)

CHOIX_CATEGORIE = (

    ('bebe','bebe'),
    ('enfant','enfant'),
    ('adulte','adulte')
)

CHOIX_PRODUIT = (
    ('pâtes', 'pâtes'),
    ('riz', 'riz'),
    ('semoule','semoule'),
    ('céréales', 'céréales'),
    ('farine','farine'),
    ('sucre', 'sucre'),
    ('oeufs','oeufs'),
    ('blancs de poulet', 'blancs de poulet'),
    ('steaks hâchés', 'steaks hâchés (boeuf)'),
    ('jambon', 'jambon (porc)'),
    ('jambon de dinde', 'jambon de dinde'),
    ('yaourt', 'yaourt'),
    ('fromage', 'fromage'),
    ('parmesan', 'parmesan râpé'),
    ('pomme', 'pomme'),
    ('banane', 'banane'),
    ('orange', 'orange'),
    ('courgette', 'courgette'),
    ('carotte', 'carotte'),
    ('pommes de terre', 'pommes de terre'),

)

CHOIX_NB_PRODUIT= (
    ('1','1 '),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20')
)



class Foyer(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=3,help_text='N° de la rue')
    rue = models.CharField(max_length=50,choices=CHOIX_RUE)
    type = models.CharField(max_length=50, choices=CHOIX_TYPE)
    nb_habitant = models.CharField(max_length=50,choices= CHOIX_NB_HABITANT,default="1")


class Utilisateur(models.Model):
    username = models.EmailField(max_length=20, default='Exemple: coronahelp@help.com')
    password = models.CharField(max_length=30, default='*******')

class Habitant(models.Model):
    nom = models.CharField(max_length=50, default='Entrez votre nom')
    prenom = models.CharField(max_length=50, default='Entrez votre prenom')
    numero_telephone = models.CharField(max_length=10, default='Entrez votre numero de telephone',null=True)
    email = models.EmailField(max_length=100,null=True)
    foyer = models.ForeignKey('Foyer', on_delete=models.CASCADE, help_text='Veuillez sélectionner le dernier foyer svp.')
    allergie = models.CharField(max_length=50,default="Aucune")
    regime = models.CharField(max_length=50,choices=CHOIX_REGIME,default='Aucun')
    categorie = models.CharField(max_length=50,choices = CHOIX_CATEGORIE,default='adulte')
    mdp = models.CharField(max_length=50, default='***********')

class Produit(models.Model):
    produit=models.CharField(max_length=50, choices=CHOIX_PRODUIT, help_text='<br> Veuillez sélectionner un produit dans la liste demandée')
    nb_produits = models.CharField(max_length=50, choices=CHOIX_NB_PRODUIT, default="1",help_text='<br>Veuillez indiquer la quantité que vous désirez')

#
# class NBProduit(models.Model):
#     nb_produits = models.CharField(max_length=50, choices=CHOIX_NB_PRODUIT, de

class Collectivite(models.Model):
    id = models.CharField(primary_key=True,max_length=15, default='Entrez votre identifiant')
    ville=models.CharField(max_length=70, default='Entrez votre ville')
    mdp = models.CharField(max_length=50, default='***********')