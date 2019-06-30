from django import forms
from callback.models import CallBack


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ('phone',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "+7 (000) 000-00-00", 'id': "CallbackPhone"}),
        }