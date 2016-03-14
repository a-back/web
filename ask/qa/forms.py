#!/usr/bin/python
# -*- coding: utf-8
#import os, sys
from django import forms
from qa.models import Question, Answer
#from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User, AnonymousUser
#from django.contrib.auth import authenticate, login

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
#    if self._user.is_anonymous():
        self.cleaned_data['author_id'] = 1
#    else:     
#      self.cleaned_data['author'] = self._user
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
        self.cleaned_data['author_id'] = 1
        #self.cleaned_data["author"] = self.user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
