from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class TelForm(ModelForm):
    class Meta:
        model = models.Tel
        fields = ('marque', 'memoire', 'date', 'prix', 'resume')
        labels = {
            'marque': _('Marque'),
            'memoire': _('Memoire'),
            'date': _('Date'),
            'prix': _('Prix'),
            'resume': _('Résumé'),
        }
