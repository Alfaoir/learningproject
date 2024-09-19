from django import forms
from .models import SoldierModel
from .models import BioModel
from .models import StudentModel




class SoldierForm(forms.ModelForm):
    class Meta:
        model = SoldierModel
        fields = [
            'title',
            "name",
            "email",
        ]
        
        
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ('firstname', 'lastname')



        
        
class BioForm(forms.ModelForm):
    class Meta: 
        model = BioModel
        fields = ('firstname', 'lastname' , 'location' , 'company' , 'favouritecar' , 'notes')
        
        
        
        
        
   