# Generated by Django 3.0.5 on 2020-05-02 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(help_text='N° de la rue', max_length=3)),
                ('rue', models.CharField(choices=[('rue de la Blanche ', ' De la Blanche'), ('rue des Ulysses', ' Des Ulysses'), ('rue de la Gare', 'De la Gare'), ('rue Jean Mermoz', 'Jean Mermoz'), ('rue Pont de Clé', 'Pont de Clé'), ('rue Aristide Brillant', 'Aristide Brillant')], max_length=50)),
                ('type', models.CharField(choices=[('maison', 'Maison'), ('appartement', 'Appartement')], max_length=50)),
                ('nb_habitant', models.CharField(choices=[('1', '1 (i.e vous)'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default='1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(default='Exemple: coronahelp@help.com', max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Habitant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='Entrez votre nom', max_length=50)),
                ('prenom', models.CharField(default='Entrez votre prenom', max_length=50)),
                ('numero_telephone', models.CharField(default='Entrez votre numero de telephone', max_length=10, null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('allergie', models.CharField(default='Aucune', max_length=50)),
                ('regime', models.CharField(choices=[('vegetarien', 'Vegetarien'), ('vegetalien', 'Vegetalien'), ('vegan', 'Vegan'), ('halal', 'Halal'), ('cacher', 'Cacher')], default='Aucun', max_length=50)),
                ('categorie', models.CharField(choices=[('bebe', 'bebe'), ('enfant', 'enfant'), ('adulte', 'adulte')], default='adulte', max_length=50)),
                ('foyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.Foyer')),
            ],
        ),
    ]
