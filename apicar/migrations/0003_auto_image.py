# Generated by Django 4.1.2 on 2022-10-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicar', '0002_rename_autos_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
