#!/usr/bin/python
# -*- coding: utf-8
#import os, sys
from django import forms
from qa.models import Question, Answer
#from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import auth 

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text =  forms.CharField(widget=forms.Textarea)
  
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip()=='':
            raise forms.ValidationError(u'Заголовок пуст', code = 11)
        return title
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip()=='':
            raise forms.ValidationError(u'Текст пуст', code = 12)
        return text
      
    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:     
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text =  forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
  
    def clean_question(self):
        question = Question.objects.get(id=self.cleaned_data['question'])
        if question is None:
            raise forms.ValidationError(u'Номер вопроса неверен', code = 21)
        return question
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip()=='':
            raise forms.ValidationError(u'Текст пуст', code = 22)
        return text
  
    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:     
            self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class LoginForm(forms.Form):
   username = forms.CharField(max_length=255)
   password = forms.CharField(widget=forms.PasswordInput) 

   def clean_username(self):
     text = self.cleaned_data['username']
     if text.strip()=='':
       raise forms.ValidationError(u'Имя пользователя пустое', code = 31)
     return text
    
   def clean_password(self):
     text = self.cleaned_data['password']
     if text.strip()=='':
       raise forms.ValidationError(u'Пароль пуст', code = 32)
     return text

   def save(self):
     user = auth.authenticate(**self.cleaned_data)
     return user

class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
   
    def clean_username(self):
        text = self.cleaned_data['username']
        if text.strip()=='':
            raise forms.ValidationError(u'Имя пользователя пустое', code = 12)
        return text
    
    def clean_password(self):
        text = self.cleaned_data['password']
        if text.strip()=='':
            raise forms.ValidationError(u'Пароль пуст', code = 12)
        return text

    def clean_email(self):
        text = self.cleaned_data['email']
        if text.strip()=='':
            raise forms.ValidationError(u'Email пустой', code = 12)
        return text

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        user = auth.authenticate(**self.cleaned_data)
        return user
