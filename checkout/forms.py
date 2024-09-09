from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        )

    # Overrides the init method to allow for customisation
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # Calls default init method to set form up as it would be by default
        super().__init__(*args, **kwargs)

        # Placeholders dict for reducing clutter in html template
        # Removes need for labels on form input fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }


        # Sets 'autofocus' attr to True so cursor is in this field by default
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Iterates through form fields and sets various values
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # Adds star if field is required
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Sets field placeholder value to corresponding placeholders
                # dict value from above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds a css class
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removes form labels as they are not needed with placeholder text
            self.fields[field].label = False
