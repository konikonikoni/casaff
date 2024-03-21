# Generated by Django 5.0b1 on 2023-11-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0015_casino_bonus_first_deposit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casino',
            options={'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='depositmethod',
            options={'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['rank']},
        ),
        migrations.AlterField(
            model_name='casino',
            name='rank',
            field=models.PositiveIntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='depositmethod',
            name='rank',
            field=models.PositiveIntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='rank',
            field=models.PositiveIntegerField(blank=True, max_length=3, null=True),
        ),
    ]
