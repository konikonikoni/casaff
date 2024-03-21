from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime, timedelta, timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class BonusType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField(null=True, blank=True)
    icon = models.FileField(upload_to="images/provider", null=True, blank=True,
                             validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']

class DepositMethod(models.Model):
    name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField(null=True, blank=True)
    icon = models.FileField(upload_to="images/deposit_method", null=True, blank=True,
                             validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']

class Casino(models.Model):
    name = models.CharField(max_length=200)
    icon = models.FileField(upload_to="images/casino_icon", null=True, blank=True,
                             validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])])
    description = models.TextField(null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    country = models.ManyToManyField(Country)
    bonus = models.CharField(max_length=10)
    bonus_type = models.ForeignKey(BonusType, on_delete=models.SET_NULL, null=True)
    bonus_max = models.CharField(max_length=10)
    bonus_wager = models.CharField(max_length=5)
    bonus_first_deposit = models.CharField(max_length=50, null=True, blank=True)
    bonus_second_deposit = models.CharField(max_length=50, null=True, blank=True)
    bonus_third_deposit = models.CharField(max_length=50, null=True, blank=True)
    bonus_code = models.CharField(max_length=20, null=True, blank=True)
    free_spins = models.CharField(max_length=5, null=True, blank=True)
    affiliate_link = models.CharField(max_length=200, default='https://slotalarm.com')
    providers = models.ManyToManyField(Provider)
    deposit_methods = models.ManyToManyField(DepositMethod)
    highlight = models.CharField(max_length=20, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_new(self):
        now = datetime.now(timezone.utc)
        return (now - self.created) < timedelta(days=14)

    class Meta:
        ordering = ['rank']