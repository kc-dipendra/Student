# Generated by Django 3.2.9 on 2023-03-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=255)),
                ('Teacher_Eudcation', models.CharField(max_length=255)),
                ('Teacher_Subject', models.CharField(max_length=255)),
            ],
        ),
    ]