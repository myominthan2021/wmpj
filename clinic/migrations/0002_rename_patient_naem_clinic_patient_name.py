# Generated by Django 3.2.9 on 2021-11-26 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='patient_naem',
            new_name='patient_name',
        ),
    ]