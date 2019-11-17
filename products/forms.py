from django import forms
from . models import Products, TYPES_CHOICES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


select_op = [('', "Select Category")]
last_ch = select_op + TYPES_CHOICES


class ProductCreateForm(forms.ModelForm):
    price = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "Placeholder": "Product Price",
            "class": "form-control",
        }), required=True)

    inch = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "Placeholder": "Product Inch form-control",
        }), required=True)

    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            "placeholder": "Product Description",
        }
    ))

    product_category = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'select-field custom-select ',
        }),
        choices=last_ch, required=True)

    class Meta:
        model = Products
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.fields["year"].label = ''


# Main Seach Form
class SearchProductForm(forms.Form):
    product_category = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'select-field custom-select ',
            'placeholder': "Category"
        }),
        choices=last_ch, required=True)

    key_word = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "placeholder": "Search ...",
            'class': 'form-fiel search-Keyword',
            "name": "search_input"
        }
    ), required=True)


PAYMENT_CHOICE = (
    ('C', "Card"),
    ('S', "Stripe")
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(
        attrs={
            "Placeholder": "Street address",
            "class": "input-field form-control"
        }
    ), label="")

    appartment_address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "Placeholder": "Appartment address (Optional)",
            "class": "input-field form-control"
        }
    ), label="")

    country = CountryField(blank_label='(select country)').formfield(
        attrs={
            "class": "input-field form-control"
        }
    )
    zip = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "placeholder": "Zip *",
            "class": "zipInput form-control input-field"
        }
    ))

    same_billing_address = forms.BooleanField(
        widget=forms.CheckboxInput, required=False, label="Same As Billing address")
    save_info = forms.BooleanField(
        widget=forms.CheckboxInput, label="Save Info", required=False,)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICE)
