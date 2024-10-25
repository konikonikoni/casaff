from django.shortcuts import render
from .models import Casino, DepositMethod, Provider, SocialMedia, BonusType, CasinoPageContent


def home(request):
    casinos = Casino.objects.all().order_by('rank')

    # Retrieve all DepositMethods, Providers, and Bonustypes instances
    all_deposit_methods = DepositMethod.objects.all()
    all_providers = Provider.objects.all()
    all_bonus_types = BonusType.objects.all()

    # Retrieve social media links
    social_media_links = SocialMedia.objects.first()

    # Retrieve SEO content
    content = CasinoPageContent.objects.first()  # Assuming a single entry

    # Sorting related data within Casino instances
    for casino in casinos:
        casino.sorted_deposit_methods = casino.deposit_methods.all().order_by('rank')
        casino.sorted_providers = casino.providers.all().order_by('rank')
        casino.bonus_type = casino.bonus_type
        casino.free_spins = casino.free_spins

    context = {
        'casinos': casinos,
        'all_bonus_types': all_bonus_types,
        'all_deposit_methods': all_deposit_methods,
        'all_providers': all_providers,
        'social_media_links': social_media_links,  # Add social media links to the context
        'welcome_text': content.welcome_text if content else "",  # Retrieve welcome text
        'info_text': content.info_text if content else "",  # Retrieve info text
    }
    return render(request, 'casinos/home.html', context)


def casino(request, pk):
    casino = Casino.objects.get(id=pk)
    context = {'casino': casino}
    return render(request, 'casinos/casino.html', context)