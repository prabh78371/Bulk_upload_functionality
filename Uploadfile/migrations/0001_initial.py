# Generated by Django 4.0.2 on 2022-09-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('image2', models.ImageField(blank=True, upload_to='images')),
                ('gst', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
    ]
