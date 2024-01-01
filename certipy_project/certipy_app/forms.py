from django import forms

class TemplateForm(forms.Form):
  templatefile = forms.FileField(label='Selecione um Template em .svg')
