# Generated by Django 4.1.7 on 2023-05-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.TextField()),
                ('activity_file', models.FileField(upload_to='static/activity')),
                ('enroll_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_title', models.TextField()),
                ('assignment_file', models.FileField(upload_to='static/assignment')),
                ('enroll_no', models.IntegerField()),
            ],
        ),
    ]