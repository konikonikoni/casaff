# Generated by Django 5.0b1 on 2023-11-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0021_casino_bonus_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='free_spins',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
