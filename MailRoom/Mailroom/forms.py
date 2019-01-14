from django import forms
from django.contrib.auth.models import User
from.import models
class Register(forms.ModelForm):
	class Meta:
		model=models.OtherUsers
		fields=('user','phone','rollNo','Mail_Id')
class Package(forms.ModelForm):
    class Meta:
        model=models.Package
        fields=('Number','Company','RollNo','Phone')
