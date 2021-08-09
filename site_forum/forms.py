from django.contrib.auth import authenticate
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

from site_forum.models import Resposta, Topico

class UserLoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': (
            "Username %(username)s ou password incorretos."
        ),
    }
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self._user = authenticate(username=username, password=password)

            if self._user is None:
                raise ValidationError(
                    self.error_messages['invalid_login'], 
                    code='invalid_login',
                    params={'username': username},)
            else:
                return cleaned_data
    
    def get_user(self):
        return self._user
            

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, initial='')
    password2 = forms.CharField(widget=forms.PasswordInput, initial='')

    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}
    
    def clean(self):
        cleaned_data = super().clean()
        password2 = cleaned_data.get('password2')
        password = cleaned_data.get('password')

        if password and password2 and (password != password2):
            self.add_error ('password2', ValidationError('Senhas diferentes'))
        else:
            return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class TopicoCreateForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'texto']
    
    def save(self, user, forum, commit=True):
        topico = super().save(commit=False)
        topico.user = user
        topico.forum = forum
        if commit:
            topico.save()
        return topico

class TopicoUpdateForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'texto']


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'
        exclude = ('user',)

    def save(self, user, commit=True):
        resposta = super().save(commit=False)
        resposta.user = user
        if commit:
            resposta.save()
        
        return resposta
        