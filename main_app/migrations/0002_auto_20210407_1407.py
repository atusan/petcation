# Generated by Django 3.1.7 on 2021-04-07 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sitter',
            new_name='sitters',
        ),
    ]
