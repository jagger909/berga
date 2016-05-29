from django.forms import ModelForm, TextInput
from main.models import Zayavka


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ('zayavka_name', 'phone_number',)
        widgets = {
            'zayavka_name': TextInput(attrs={'placeholder': u'имя'}),
            'phone_number': TextInput(attrs={'placeholder': u'телефон'}),

        }
