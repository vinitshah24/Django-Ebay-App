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
            product_id = form.cleaned_data.get('product_id')
            product_count = form.cleaned_data.get('product_count')
            start_date = form.cleaned_data.get('start_date')
            category = form.cleaned_data.get('category')

            print(product_id)
            print(str(product_count))
            print(start_date)  # 2000-04-01
            print(category)

            raw_data = utils.api_query(search_query)
            products = utils.get_data(raw_data)
            context = {'products': products, 'form': form}
    else:
        form = forms.SearchProducts()
        context = {'form': form}
    return render(request, 'store/store.html', context)
