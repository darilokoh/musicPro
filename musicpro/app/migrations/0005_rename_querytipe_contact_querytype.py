# Generated by Django 4.2 on 2023-04-26 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_querytipe_querytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='queryTipe',
            new_name='queryType',
        ),
    ]
