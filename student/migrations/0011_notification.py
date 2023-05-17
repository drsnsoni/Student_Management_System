# Generated by Django 4.1.7 on 2023-05-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/notification')),
                ('date', models.DateField()),
            ],
        ),
    ]