from django import forms
from .models import Character

class Character(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__' 
        exclude= ['player']
        widgets = {
            'name': forms.TextInput(attrs={'class':'text-form','id': 'name-form', 'placeholder': 'Name'}),
            'race': forms.TextInput(attrs={'class':'text-form','id': 'race-form', 'placeholder': 'Race'}),
            'classes': forms.TextInput(attrs={'class':'text-form','id': 'classes-form', 'placeholder': 'Classes'}),
            'background': forms.TextInput(attrs={'class':'text-form','id': 'background-form', 'placeholder': 'Background'}),
            'alignment': forms.TextInput(attrs={'class':'text-form','id': 'alignment-form', 'placeholder': 'Alignment'}),
            'strength': forms.NumberInput(attrs={'id': 'strength-form', 'class':'number-form', 'placeholder': '10'}),
            'dexterity': forms.NumberInput(attrs={'id': 'dexterity-form', 'class':'number-form', 'placeholder': '10'}),
            'constitution': forms.NumberInput(attrs={'id': 'constitution-form','class':'number-form', 'placeholder': '10'}),
            'intelligence': forms.NumberInput(attrs={'id': 'intelligence-form','class':'number-form', 'placeholder': '10'}),
            'wisdom': forms.NumberInput(attrs={'id': 'wisdom-form','class':'number-form', 'placeholder': '10'}),
            'carisma': forms.NumberInput(attrs={'id': 'carisma-form','class':'number-form', 'placeholder': '10'}),
            'hitpoints': forms.NumberInput(attrs={'id': 'hitpoints-form','class':'number-form', 'placeholder': '0'}),
            'level': forms.NumberInput(attrs={'id': 'level-form','class':'number-form', 'placeholder': '1'}),
            'description': forms.Textarea(attrs={'class':'textarea-form','id': 'description-form', 'placeholder': 'Description (Optional)'}),
            'inventory': forms.Textarea(attrs={'class':'textarea-form','id': 'inventory-form', 'placeholder': 'Inventory (Optional)'}),
            'image' : forms.Select(attrs={'class':'portrait-form', 'id':'image-form'})
        }
