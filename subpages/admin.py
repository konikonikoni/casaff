# subpages/admin.py

from django import forms
from django.contrib import admin
from .models import Subpage, SubpageCasino

class SubpageCasinoInline(admin.TabularInline):  # Or use admin.StackedInline for a more detailed display
    model = SubpageCasino
    extra = 1  # Number of extra inline forms to display

class SubpageAdminForm(forms.ModelForm):
    class Meta:
        model = Subpage
        fields = ['title', 'css_file', 'youtube', 'facebook', 'twitch', 'instagram', 'dlive', 'kick']  # Exclude casinos field

class SubpageAdmin(admin.ModelAdmin):
    form = SubpageAdminForm
    inlines = [SubpageCasinoInline]

admin.site.register(Subpage, SubpageAdmin)
