# Generated by Django 5.0b1 on 2023-11-13 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0018_bonustype_remove_casino_bonus_type_casino_bonus_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonustype',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='bonustype',
            name='rank',
        ),
    ]
