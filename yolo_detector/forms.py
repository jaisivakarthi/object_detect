from django import forms  
from yolo_detector.models import TblAdmin  
class loginform(forms.ModelForm):  
    class Meta:  
        model = TblAdmin  
        fields = "__all__"
class changepasswordform(forms.ModelForm):  
    class Meta:  
        model = TblAdmin  
        fields = "__all__"
