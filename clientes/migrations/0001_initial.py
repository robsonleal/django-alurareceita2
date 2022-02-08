# Generated by Django 4.0.2 on 2022-02-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9)),
                ('celular', models.CharField(max_length=14)),
                ('ativo', models.BooleanField()),
            ],
        ),
    ]
