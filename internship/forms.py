from django import forms
from .models import Think_Analytics




class info_form(forms.ModelForm):
	class Meta:
		model=Think_Analytics
		fields= '__all__'
