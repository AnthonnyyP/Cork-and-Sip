# Generated by Django 4.2.2 on 2023-06-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_wine_name_collection_producer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasting',
            name='time',
            field=models.CharField(choices=[('M', '11:30 AM'), ('A', '2:00 PM'), ('N', '6:00 PM')], default='M', max_length=1),
        ),
    ]
