# Generated by Django 2.2.4 on 2019-09-04 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='contact_date',
        ),
    ]
