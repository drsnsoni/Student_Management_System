# Generated by Django 4.1.7 on 2023-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_attendance_products_store_upcoming_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcoming',
            name='event_banner',
            field=models.ImageField(blank=True, upload_to='static/event'),
        ),
    ]
