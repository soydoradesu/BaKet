# Generated by Django 5.1.2 on 2024-10-27 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
