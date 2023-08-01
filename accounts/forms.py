from django import forms
# from shop import models
#
# # class UserForm(forms.ModelForm):
# #     class Meta:
# #         model = User
# #         fields = ('username', 'password1', 'password2', 'phonenum', 'birthY', 'birthM', 'birthD')
#
# class UserForm(forms.Form):
#     username = forms.CharField(max_length=80)
#     nickname = forms.CharField(max_length=80)
#     password = forms.CharField(widget=forms.PasswordInput)
#     password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
#     birthY = forms.IntegerField(max_value=2100)
#     birthM = forms.IntegerField(max_value=12)
#     birthD = forms.IntegerField(max_value=32)
#
#     def clean_password1(self):
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")
#         if password != password1:
#             raise forms.ValidationError("Password confirmation does not match")
#         else:
#             return password
#
#     def save(self):
#         username = self.cleaned_data.get("username")
#         nickname = self.cleaned_data.get("nickname")
#         birthY = self.cleaned_data.get("birthY")
#         birthM = self.cleaned_data.get("birthM")
#         birthD = self.cleaned_data.get("birthD")
#         password = self.cleaned_data.get("password")
#         phonenum = self.cleaned_data.get("phonenum")
#         user = models.User.objects.create_user(username, nickname, birthD, birthM, birthY, password, phonenum)
#         user.nickname = nickname
#         user.save()


# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from wheel.metadata import _

from accounts.models import Account, MyAccountManager


# 회원 가입 폼
class RegistrationForm(UserCreationForm):
    phonenum = forms.IntegerField(help_text='올바른 핸드폰 번호를 입력해 주세요.')
    password1 = forms.CharField(label=_('비밀번호'),
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':_('비밀번호'),
                                        'required': 'True',
                                    }
                                ))
    password2 = forms.CharField(label=_('비밀번호 확인'),
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': _('비밀번호 확인'),
                                        'required': 'True',
                                    }
                                ))

    class Meta:
        model = Account
        fields = ('phonenum', 'username', 'nickname', 'birthY', 'birthM', 'birthD',)

    def clean_phonenum(self):
        phonenum = self.cleaned_data['phonenum']
        try:
            account = Account.objects.get(phonenum=phonenum)
        except Exception as e:
            return phonenum
        raise forms.ValidationError(f"핸드폰 번호 {phonenum}는 이미 사용되고 있습니다.")

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        try:
            account = Account.objects.get(nickname = nickname)
        except Exception as e:
            return nickname
        raise forms.ValidationError(f"별명 {nickname}은 이미 사용되고 있습니다.")

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 다릅니다.")
        return password2


# 로그인 인증 폼
class AccountAuthForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('phonenum', 'password')

    def clean(self):
        if self.is_valid():
            phonenum = self.cleaned_data['phonenum']
            password = self.cleaned_data['password']
            if not authenticate(phonenum=phonenum, password=password):
                raise forms.ValidationError("로그인 실패")