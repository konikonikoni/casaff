# Generated by Django 5.0b1 on 2023-10-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0005_depositmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='deposit_methods',
            field=models.ManyToManyField(to='casinos.depositmethod'),
        ),
        migrations.AddField(
            model_name='casino',
            name='providers',
            field=models.ManyToManyField(to='casinos.provider'),
        ),
    ]