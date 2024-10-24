# subpages/views.py

from django.shortcuts import render, get_object_or_404
from .models import Subpage

def subpage_detail(request, subpage_name):
    subpage = get_object_or_404(Subpage, title=subpage_name)
    casinos = subpage.casinos.all()  # Get all casinos associated with the subpage
    return render(request, 'main.html', {'subpage': subpage, 'casinos': casinos})
