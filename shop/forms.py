from django import forms
from . import models

app_name = 'shop'
...
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'phonenum', 'birthY', 'birthM', 'birthD')

class UserForm(forms.Form):
    username = forms.CharField(max_length=80)
    nickname = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
    birthY = forms.IntegerField(max_value=2100)
    birthM = forms.IntegerField(max_value=12)
    birthD = forms.IntegerField(max_value=32)

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        username = self.cleaned_data.get("username")
        nickname = self.cleaned_data.get("nickname")
        birthY = self.cleaned_data.get("birthY")
        birthM = self.cleaned_data.get("birthM")
        birthD = self.cleaned_data.get("birthD")
        password = self.cleaned_data.get("password")
        phonenum = self.cleaned_data.get("phonenum")
        user = models.User.objects.create_user(username, nickname, birthD, birthM, birthY, password, phonenum)
        user.nickname = nickname
        user.save()