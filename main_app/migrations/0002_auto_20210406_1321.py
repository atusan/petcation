# Generated by Django 3.1.7 on 2021-04-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sitters',
            field=models.ManyToManyField(blank=True, null=True, to='main_app.Sitter'),
        ),
    ]