# Generated by Django 2.0.7 on 2020-05-24 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='owner',
        ),
    ]
