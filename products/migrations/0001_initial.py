# Generated by Django 5.1.4 on 2024-12-21 09:56

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
                ('nomi', models.CharField(max_length=100)),
                ('tavsif', models.TextField()),
                ('narxi', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('kategoriya', models.CharField(max_length=50)),
            ],
        ),
    ]
