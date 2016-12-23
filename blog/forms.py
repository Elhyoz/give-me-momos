# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from blog.models import Momo


class MomoForm(forms.ModelForm):
    class Meta:
        model = Momo
        fields = '__all__'
