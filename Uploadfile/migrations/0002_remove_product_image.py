# Generated by Django 4.0.2 on 2022-09-28 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Uploadfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]