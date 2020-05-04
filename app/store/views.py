from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import utils
from . import forms


@login_required
def store(request):
    if request.method == 'POST':
        form = forms.SearchProducts(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            product_count = form.cleaned_data.get('product_count')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')

            if search_query is not None and search_query != '' \
                    and product_count > 1 and min_price > 0 and max_price > 0:
                raw_data = utils.api_query(query=search_query,
                                           numberOfProducts=product_count,
                                           minPrice=min_price,
                                           maxPrice=max_price)
            elif search_query is not None and search_query != ''\
                    and min_price > 0 and max_price > 0:
                raw_data = utils.api_query(query=search_query,
                                           minPrice=min_price,
                                           maxPrice=max_price)
            elif search_query is not None and search_query != '' \
                    and product_count > 1:
                raw_data = utils.api_query(query=search_query,
                                           numberOfProducts=product_count)
            elif search_query is not None and search_query != '' \
                    and min_price > 0:
                raw_data = utils.api_call = utils.api_query(query=search_query,
                                                            minPrice=min_price)
            elif search_query is not None and search_query != '' \
                    and max_price > 0:
                raw_data = utils.api_query(query=search_query,
                                           maxPrice=max_price)
            elif search_query is not None and search_query != '':
                raw_data = utils.api_query(query=search_query)
            else:
                raw_data = None

            if raw_data is not None:
                products = utils.get_data(raw_data)
                if products:
                    context = {'products': products, 'form': form}
            else:
                form = forms.SearchProducts()
                context = {'form': form}
    else:
        form = forms.SearchProducts()
        context = {'form': form}
    try:
        if context is None:
            form = forms.SearchProducts()
            context = {'form': form}
    except:
        context = {}
        messages.warning(request, f'Items not found!')
        form = forms.SearchProducts()
        if form:
            context = {'form': form}
        pass
    return render(request, 'store/store.html', context)
