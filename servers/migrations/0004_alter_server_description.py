# Generated by Django 5.0.4 on 2024-05-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_alter_server_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
