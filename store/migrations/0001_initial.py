# Generated by Django 2.0.2 on 2019-01-19 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Catégorie')),
                ('icone', models.ImageField(upload_to='photo/', verbose_name='Icone')),
            ],
            options={
                'verbose_name_plural': 'Catégories',
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200, verbose_name='Prénom')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
            ],
            options={
                'verbose_name_plural': 'Commandes',
                'verbose_name': 'Commande',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de commande')),
                ('validation', models.BooleanField(default=True, verbose_name='Validation')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Contact')),
            ],
            options={
                'verbose_name_plural': 'Commandes',
                'verbose_name': 'Commande',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_photo', models.ImageField(upload_to='photo/', verbose_name='Photos')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('short', models.CharField(blank=True, max_length=200, verbose_name='Description courte')),
                ('long', models.TextField(verbose_name='Description longue')),
                ('image', models.ImageField(upload_to='photo/', verbose_name='Image')),
                ('price1', models.CharField(blank=True, max_length=200, verbose_name='Prix du marché')),
                ('price', models.CharField(max_length=200, verbose_name='Prix réel')),
                ('reduction', models.IntegerField(blank=True, default=0, verbose_name='Réduction')),
                ('stock', models.IntegerField(blank=True, default=0, verbose_name='Stock')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Categorie')),
            ],
            options={
                'verbose_name_plural': 'Produits',
                'verbose_name': 'Produit',
            },
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='photo/')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AddField(
            model_name='img',
            name='pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Pub'),
        ),
    ]
