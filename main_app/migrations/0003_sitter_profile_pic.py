# Generated by Django 3.1.7 on 2021-04-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/css/images'),
        ),
    ]
