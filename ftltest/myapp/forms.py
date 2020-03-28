from django import forms
from myapp.models import user,activity_periods

class PostForm(forms.ModelForm):

    class Meta:
        model = user
        fields = '__all__'
        
class NewForm(forms.ModelForm):

    class Meta:
        model = activity_periods
        fields = '__all__'