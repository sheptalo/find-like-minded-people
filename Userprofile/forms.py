from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль')
    next = forms.CharField(widget=forms.HiddenInput(), required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    email = forms.CharField(label=u'e-mail')
    password = forms.CharField(label=u'Пароль')
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
