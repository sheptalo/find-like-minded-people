from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Имя пользователя'}),
                               max_length=20)
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))
    next = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'next'}), required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Имя пользователя'}),
                               max_length=20)
    email = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Почта'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
