# Generated by Django 4.1.2 on 2022-10-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicar', '0003_auto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/', verbose_name='Image'),
        ),
    ]
