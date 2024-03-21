from django.shortcuts import render
from .models import Casino, DepositMethod, Provider

# Create your views here.

def home(request):
    casinos = Casino.objects.all().order_by('rank')

    # Retrieve all DepositMethod and Provider instances
    all_deposit_methods = DepositMethod.objects.all()
    all_providers = Provider.objects.all()

    for casino in casinos:
        casino.sorted_deposit_methods = casino.deposit_methods.all().order_by('rank')
        casino.sorted_providers = casino.providers.all().order_by('rank')

    context = {
        'casinos': casinos,
        'all_deposit_methods': all_deposit_methods,
        'all_providers': all_providers,
    }
    return render(request, 'casinos/home.html', context)

def casino(request, pk):
    casino = Casino.objects.get(id=pk)
    context = {'casino': casino}
    return render(request, 'casinos/casino.html', context)