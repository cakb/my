# Generated by Django 2.0.2 on 2019-02-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20190131_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='validation',
            field=models.BooleanField(default=False, verbose_name='Validation'),
        ),
    ]
