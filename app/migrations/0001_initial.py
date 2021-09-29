# Generated by Django 3.2.7 on 2021-09-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('marca', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
