# Generated by Django 5.0b1 on 2023-10-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0004_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
