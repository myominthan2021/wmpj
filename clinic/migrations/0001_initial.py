# Generated by Django 3.2.9 on 2021-11-26 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_naem', models.CharField(max_length=255)),
                ('patient_phone', models.CharField(max_length=255)),
                ('patient_address', models.TextField()),
                ('patient_case', models.TextField()),
                ('fileupload', models.FileField(upload_to='files')),
                ('drug', models.TextField()),
                ('fees', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datetime', models.DateTimeField()),
                ('doctor', models.CharField(max_length=255)),
            ],
        ),
    ]
