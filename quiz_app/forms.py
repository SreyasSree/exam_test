from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Check if the phone number is exactly 10 digits
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number should be 10 digits long.")

        # Additional checks for a valid mobile number can be added here
        # For example, checking if it consists only of digits, or if it follows a specific format

        return phone_number