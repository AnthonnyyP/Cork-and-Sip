# Generated by Django 4.2.2 on 2023-06-20 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_tasting_delete_winetasting_guest_wine_tasting_guest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='user_email',
            new_name='user_Email',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='user_phone',
            new_name='user_Phone',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='user_name',
            new_name='username',
        ),
    ]
