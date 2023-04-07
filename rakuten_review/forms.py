from django import forms
from .models import WeeklyRanking

class WeeklyRankingForm(forms.ModelForm):

    class Meta:
        model   = WeeklyRanking
        fields  = [ "update_date","name","price","average","volume","rank","shop_code","item_url" ]

