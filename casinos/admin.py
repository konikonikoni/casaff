from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.http import HttpResponseRedirect
from .models import Casino, Provider, DepositMethod, BonusType, Country, SocialMedia, CasinoPageContent

# Register CasinoPageContent with welcome and info fields, allowing only one instance
@admin.register(CasinoPageContent)
class CasinoPageContentAdmin(admin.ModelAdmin):
    fields = ('welcome_text', 'info_text')

    def has_add_permission(self, request):
        # Prevents creating a new instance if one already exists
        return not CasinoPageContent.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # Redirect to the edit page of the single instance
        try:
            content = CasinoPageContent.objects.get()
            return HttpResponseRedirect(f"/admin/casinos/casinopagecontent/{content.id}/change/")
        except CasinoPageContent.DoesNotExist:
            return super().changelist_view(request, extra_context=extra_context)

# Register Casino model with sorting and customization
@admin.register(Casino)
class SortableCasino(SortableAdminMixin, admin.ModelAdmin):
    filter_horizontal = ('deposit_methods', 'providers',)
    list_display = ('name', 'get_ordering_number',)
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank
    get_ordering_number.short_description = 'Order'

# Register Provider model with sorting and customization
@admin.register(Provider)
class SortableProvider(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_ordering_number',)
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank
    get_ordering_number.short_description = 'Order'

# Register DepositMethod model with sorting and customization
@admin.register(DepositMethod)
class SortableDepositMethod(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_ordering_number',)
    search_fields = ['name']

    def get_ordering_number(self, obj):
        return obj.rank
    get_ordering_number.short_description = 'Order'

# Register additional models without customization
admin.site.register(BonusType)
admin.site.register(Country)
admin.site.register(SocialMedia)