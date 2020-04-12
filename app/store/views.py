from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import utils
from . import forms

@login_required
def store(request):
    if request.method == 'POST':
        form = forms.SearchProducts(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            raw_data = utils.api_query(search_query)
            products = utils.get_data(raw_data)
            context = {'products': products, 'form': form}
    else:
        form = forms.SearchProducts()
        context = {'form': form}
    return render(request, 'store/store.html', context)
