# Generated by Django 3.0.5 on 2020-05-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_auto_20200503_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitant',
            name='allergie',
            field=models.CharField(default='Aucune', max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='categorie',
            field=models.CharField(choices=[('bebe', 'bebe'), ('enfant', 'enfant'), ('adulte', 'adulte')], default='adulte', max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='nom',
            field=models.CharField(default='Entrez votre nom', max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='numero_telephone',
            field=models.CharField(default='Entrez votre numero de telephone', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='prenom',
            field=models.CharField(default='Entrez votre prenom', max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='regime',
            field=models.CharField(choices=[('aucun', 'Aucun'), ('vegetarien', 'Vegetarien'), ('vegetalien', 'Vegetalien'), ('vegan', 'Vegan'), ('halal', 'Halal'), ('cacher', 'Cacher')], default='Aucun', max_length=50),
        ),
    ]