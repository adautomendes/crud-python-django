# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

#Specialization
def spec_list_all(request):
    return render(request, 'crud/spec_index.html')
def ajax_spec_list_all(request):
    specs_json = serializers.serialize('json', Specialization.objects.all())
    return HttpResponse(specs_json, content_type='application/json')

def spec_new(request):
    return render(request, 'crud/spec_form.html')
def ajax_spec_new(request):
    specs_json = serializers.serialize('json', Specialization.objects.all())
    return HttpResponse(specs_json, content_type='application/json')

def spec_edit(request):
    # Receive id from spec
    return render(request, 'crud/spec_form.html')
def ajax_spec_edit(request):
    specs_json = serializers.serialize('json', Specialization.objects.all())
    return HttpResponse(specs_json, content_type='application/json')

def spec_delete(request):
    return render(request, 'crud/spec_index.html')
def ajax_spec_delete(request):
    id = request.POST.get('id', None)

    specs_json = serializers.serialize('json', Specialization.objects.all())
    return HttpResponse(id, content_type='application/json')

#Character
def char_list_all(request):
    return render(request, 'crud/char_index.html')
def ajax_char_list_all(request):
    chars_json = serializers.serialize('json', Character.objects.all())
    return HttpResponse(chars_json, content_type='application/json')

def char_new(request):
    return render(request, 'crud/char_form.html')
def ajax_char_new(request):
    chars_json = serializers.serialize('json', Character.objects.all())
    return HttpResponse(chars_json, content_type='application/json')

def char_edit(request):
    # Receive id from char
    return render(request, 'crud/char_form.html')
def ajax_char_edit(request):
    chars_json = serializers.serialize('json', Character.objects.all())
    return HttpResponse(chars_json, content_type='application/json')

def char_delete(request):
    return render(request, 'crud/char_index.html')
def ajax_char_delete(request):
    chars_json = serializers.serialize('json', Character.objects.all())
    return HttpResponse(chars_json, content_type='application/json')