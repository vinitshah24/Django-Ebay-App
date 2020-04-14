from django import forms


class SearchProducts(forms.Form):
    search_query = forms.CharField(
        max_length=50,
        label='Search Query',
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
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
        widget=forms.SelectDateWidget(
            years=[y for y in range(2000, 2021)],
            attrs={'class': "form-control mb-1"}
        )
    )
    end_date = forms.DateField(
        required=False,
        label='Auction End Date',
        widget=forms.SelectDateWidget(
            years=[y for y in range(2000, 2021)],
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
