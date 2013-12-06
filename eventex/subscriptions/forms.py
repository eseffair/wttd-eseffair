# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription

#Jeito manual de fazer form
#class SubscriptionForm(forms.Form):
#    name = forms.CharField(label=_('Nome'))
#    cpf = forms.CharField(label=_('CPF'), max_length=11)
#    email = forms.EmailField(label=_('Email'))
#    phone = forms.CharField(label=_('Telefone'))

#Jeito automático de fazer form, ideal para quando o form é parecido com o model
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
