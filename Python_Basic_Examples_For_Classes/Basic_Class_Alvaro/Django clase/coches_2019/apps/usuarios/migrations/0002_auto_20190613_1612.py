# Generated by Django 2.2.2 on 2019-06-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='tipo',
            field=models.CharField(choices=[('v', 'Vendedor'), ('a', 'Admin')], max_length=20),
        ),
    ]
