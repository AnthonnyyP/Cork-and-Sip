# Generated by Django 4.2.2 on 2023-06-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('user_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_name', models.CharField(max_length=50)),
                ('wine_age', models.CharField(max_length=50)),
                ('wine_origin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WineTasting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
