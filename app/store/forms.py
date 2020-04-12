from django import forms


class SearchProducts(forms.Form):
    search_query = forms.CharField(
        max_length=50,
        required=True
    )
