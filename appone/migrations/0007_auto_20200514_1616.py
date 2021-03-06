# Generated by Django 3.0.3 on 2020-05-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0006_collectivite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='nb_produits',
            field=models.CharField(choices=[('1', '1 '), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='1', help_text='<br>Veuillez indiquer la quantité que vous désirez', max_length=50),
        ),
        migrations.AlterField(
            model_name='produit',
            name='produit',
            field=models.CharField(choices=[('pâtes', 'pâtes'), ('riz', 'riz'), ('semoule', 'semoule'), ('céréales', 'céréales'), ('farine', 'farine'), ('sucre', 'sucre'), ('oeufs', 'oeufs'), ('blancs de poulet', 'blancs de poulet'), ('steaks hâchés', 'steaks hâchés (boeuf)'), ('jambon', 'jambon (porc)'), ('jambon de dinde', 'jambon de dinde'), ('yaourt', 'yaourt'), ('fromage', 'fromage'), ('parmesan', 'parmesan râpé'), ('pomme', 'pomme'), ('banane', 'banane'), ('orange', 'orange'), ('courgette', 'courgette'), ('carotte', 'carotte'), ('pommes de terre', 'pommes de terre')], help_text='<br> Veuillez sélectionner un produit dans la liste demandée', max_length=50),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='password',
            field=models.CharField(default='*******', max_length=30),
        ),
    ]
