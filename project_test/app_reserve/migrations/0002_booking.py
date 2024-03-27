# Generated by Django 3.2.25 on 2024-03-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('subject', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
            ],
        ),
    ]
