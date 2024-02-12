from django import forms
from django.forms import inlineformset_factory
from django.forms.widgets import SelectDateWidget
from .models import Icon, Profile, Portfolio, Testimony

class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ['name','icon']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile']
    
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name','title','category','img',
                  'img2','img3','img4','img5','img6','img7',
                  'img8','img9','img10','description','client','project_date']
        widgets = {'project_date': SelectDateWidget()}

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['name','designation','testimony','picture']

