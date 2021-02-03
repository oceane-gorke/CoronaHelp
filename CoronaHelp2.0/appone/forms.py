from django import forms
from appone.models import Foyer
from appone.models import Habitant
from appone.models import Produit
from django.forms import formset_factory
#from appone.models import NBProduitt

class Foyer(forms.ModelForm):
    class Meta:
        model =Foyer
        fields = ['numero','rue','type','nb_habitant']

class Habitant(forms.ModelForm):
    class Meta:
        model = Habitant
        fields = ['nom','prenom','numero_telephone','email','allergie','regime','categorie','foyer','mdp']

#
# class NBProduit(forms.ModelForm):
#     class Meta:
#         model=NBProduit
# #         fields=['nb_produits']
# produit_formset_class = formset(
#     Produit,
#     extra=3,
#     form=ProduitForm
# )
class Produit(forms.ModelForm):
    #field1 = forms.ModelChoiceField(queryset=Produit, empty_label="------")
    class Meta:
        model=Produit
        fields=['nb_produits','produit']

#     def __init__(self, *args, **kwargs):
#         super(ProduitForm, self).__init__(*args, **kwargs)
#         produit = kwargs.get('instance', None)
#
#         if produit != None:
#             if produit.customer != None:
#                 self.fields['produit'].queryset = \
#                     produit.customer.facilities.order_by('name')
#
# ArticleFormSet=formset_factory(Produit, extra=2, min_num=1, validate_min=True)
# formset=ArticleFormSet()
# for form in formset:
#     print(form.as_table())

