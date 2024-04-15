# Generated by Django 4.2.6 on 2024-04-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0024_remove_casino_country_casino_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitch', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('dlive', models.URLField(blank=True, null=True)),
                ('kick', models.URLField(blank=True, null=True)),
            ],
        ),
    ]