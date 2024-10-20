# Generated by Django 5.1.1 on 2024-10-19 13:32

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
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('category', models.CharField(choices=[('laptop', 'Laptop'), ('smart_watch', 'Smart Watch'), ('smart_tv', 'Smart TV'), ('handphone', 'Handphone'), ('tablet', 'Tablet')], max_length=50)),
            ],
        ),
    ]
