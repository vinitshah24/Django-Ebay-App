from django import forms


class SearchProducts(forms.Form):
    search_query = forms.CharField(
        max_length=50,
        label='Search Query',
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
