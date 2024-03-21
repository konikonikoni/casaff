# Generated by Django 5.0b1 on 2023-11-05 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0011_alter_casino_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositmethod',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/deposit_method', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/provider', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg'])]),
        ),
    ]
