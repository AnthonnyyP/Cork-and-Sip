# Generated by Django 4.2.2 on 2023-06-20 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_user_email_guest_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='wine_name',
            new_name='producer',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='wine_name',
            new_name='producer',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='wine_origin',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='wine_age',
            new_name='vintage',
        ),
    ]
