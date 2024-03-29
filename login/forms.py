from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Loginform(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs=({'class':'form-control','placeholder':'请输入用户名！'})))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码！'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('你输入的用户不存在')
        if user is None:
            raise forms.ValidationError('密码不正确！')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data
