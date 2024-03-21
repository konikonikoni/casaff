from django.contrib import admin
from django.db import models
from adminsortable2.admin import SortableAdminMixin
from .models import Casino, Provider, DepositMethod, BonusType, Country


@admin.register(Casino)
class SortableCasino(SortableAdminMixin, admin.ModelAdmin):
    filter_horizontal = ('deposit_methods', 'providers',)
    list_display = ('name', 'get_ordering_number',)  # Add 'get_ordering_number' to list_display
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank

    get_ordering_number.short_description = 'Order'

@admin.register(Provider)
class SortableProvider(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_ordering_number',)  # Add 'get_ordering_number' to list_display
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank

    get_ordering_number.short_description = 'Order'

@admin.register(DepositMethod)
class SortableDepositMethod(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_ordering_number',)  # Add 'get_ordering_number' to list_display
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank

    get_ordering_number.short_description = 'Order'

admin.site.register(BonusType)

admin.site.register(Country)
