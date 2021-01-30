from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    date_started = forms.DateField(
                                    widget=forms.TextInput(attrs={'autocomplete':'off', 'class': 'date-picker'}),
                                    input_formats=['%Y/%m/%d']
                                )
    date_completed = forms.DateField(
                                        widget=forms.TextInput(attrs={'autocomplete':'off', 'class': 'date-picker'}),
                                        input_formats=['%Y/%m/%d'],
                                        required=False
                                    )

    def clean(self):
        cleaned_data = super().clean()
        completed = cleaned_data.get('completed')
        date_completed = cleaned_data.get('date_completed')
        if completed and not date_completed:
            raise forms.ValidationError("Please enter completion date for completed items")
        return cleaned_data

    class Meta:
        model = Item
        fields = ['cover_art', 'title', 'series', 'genre', 'completed', 'date_started', 'date_completed']