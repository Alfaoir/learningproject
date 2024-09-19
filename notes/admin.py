from django.contrib import admin
from .models import SoldierModel
from .models import BioModel,StudentModel
from .form import SoldierForm
from .form import BioForm
from .form import StudentForm




class SoldierModelAdmin(admin.ModelAdmin):
    form = SoldierForm
    list_display = ['title', 'name', 'email']
   

admin.site.register(SoldierModel, SoldierModelAdmin)






class BioModelAdmin(admin.ModelAdmin):
    form = BioForm
    list_display = ['firstname','lastname','location','company','favouritecar','notes'] 
    
    
admin.site.register(BioModel, BioModelAdmin)




class StudentModelAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['firstname','lastname'] 
    
    
admin.site.register(StudentModel, StudentModelAdmin)