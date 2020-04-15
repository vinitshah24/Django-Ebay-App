from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchProducts(forms.Form):
    search_query = forms.CharField(
        max_length=50,
        label='Search Query',
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    product_count = forms.IntegerField(
        required=False,
        initial=1,
        min_value=1,
        max_value=100,
        label='Products Count',
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    min_price = forms.IntegerField(
        required=False,
        initial=0,
        min_value=0,
        max_value=100000,
        label='Mininum Product Price',
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    max_price = forms.IntegerField(
        required=False,
        initial=0,
        min_value=0,
        max_value=100000,
        label='Maximum Product Price',
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    """
    product_id = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Product ID',
            'class': "form-control border-right-0 border"
        })
    )
    product_count = forms.IntegerField(
        required=False,
        initial=1,
        min_value=1,
        max_value=100,
        label='Count',
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    start_date = forms.DateField(
        required=False,
        label='Auction Start Date',
        widget=DateInput(
            attrs={'class': "form-control mb-1"}
        )
    )
    end_date = forms.DateField(
        required=False,
        label='Auction End Date',
        widget=DateInput(
            attrs={'class': "form-control mb-1"}
        )
    )
    category = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': "form-control"
        })
    )
    """
