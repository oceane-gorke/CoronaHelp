# Generated by Django 3.0.5 on 2020-05-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitant',
            name='allergie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='categorie',
            field=models.CharField(choices=[('bebe', 'bebe'), ('enfant', 'enfant'), ('adulte', 'adulte')], max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='numero_telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='prenom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='regime',
            field=models.CharField(choices=[('vegetarien', 'Vegetarien'), ('vegetalien', 'Vegetalien'), ('vegan', 'Vegan'), ('halal', 'Halal'), ('cacher', 'Cacher')], max_length=50),
        ),
    ]
