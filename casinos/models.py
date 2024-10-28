from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field  # Import CKEditor5Field from django_ckeditor_5
from datetime import datetime, timedelta, timezone

class CasinoSpotlight(models.Model):
    casino = models.ForeignKey('Casino', on_delete=models.CASCADE, related_name="spotlight")
    promo_text = CKEditor5Field("Promotional Text", blank=True, help_text="Text for the spotlight casino", config_name="default")

    def __str__(self):
        return f"Spotlight for {self.casino.name}"

class CasinoPageContent(models.Model):
    welcome_text = CKEditor5Field("Welcome Text", blank=True, help_text="Text for the welcome section", config_name="default")
    info_text = CKEditor5Field("SEO Info Text", blank=True, help_text="SEO-optimized text for the bottom of the page", config_name="default")

    def save(self, *args, **kwargs):
        if not self.pk and CasinoPageContent.objects.exists():
            raise ValueError("Only one instance of CasinoPageContent is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Casino Page Content"

class SocialMedia(models.Model):
    youtube = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitch = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    dlive = models.URLField(max_length=200, null=True, blank=True)
    kick = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Social Media Links"

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
    icon = models.FileField(
        upload_to="images/provider",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])]
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']

class DepositMethod(models.Model):
    name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField(null=True, blank=True)
    icon = models.FileField(
        upload_to="images/deposit_method",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])]
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']

class Casino(models.Model):
    name = models.CharField(max_length=200)
    icon = models.FileField(
        upload_to="images/casino_icon",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'])]
    )
    description = models.TextField(null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    country = models.ManyToManyField(Country)
    bonus = models.CharField(max_length=10)
    bonus_type = models.ForeignKey(BonusType, on_delete=models.SET_NULL, null=True, blank=True)
    bonus_code = models.CharField(max_length=20, null=True, blank=True)
    bonus_max = models.CharField(max_length=10)
    bonus_wager = models.CharField(max_length=5)
    free_spins = models.CharField(max_length=5, null=True, blank=True)
    affiliate_link = models.CharField(max_length=200, default='https://slotalarm.com')
    providers = models.ManyToManyField(Provider)
    deposit_methods = models.ManyToManyField(DepositMethod)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_new(self):
        now = datetime.now(timezone.utc)
        return (now - self.created) < timedelta(days=14)

    class Meta:
        ordering = ['rank']