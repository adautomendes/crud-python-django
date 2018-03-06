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

def spec_edit(request, spec_id):
    # Receive id from spec
    specialization = Specialization.objects.get(pk=spec_id)
    return render(request, 'crud/spec_form.html', { 'specialization' : specialization })

def spec_save(request):
    pk = request.POST.get('pk', None)
    name = request.POST.get('name', None)
    initial_life = request.POST.get('initial_life', None)
    initial_mana = request.POST.get('initial_mana', None)

    if pk is "": #Creating new
        specialization = Specialization(name=name, initial_life=initial_life, initial_mana=initial_mana)
    else: #Editing
        specialization = Specialization(pk=pk, name=name, initial_life=initial_life, initial_mana=initial_mana)

    specialization.save()
    return render(request, 'crud/spec_index.html')

def spec_delete(request):
    return render(request, 'crud/spec_index.html')

def ajax_spec_delete(request):
    id = request.POST.get('id', None)
    specialization = Specialization.objects.get(pk=id)
    specialization.delete()

    specs_json = serializers.serialize('json', Specialization.objects.all())
    return HttpResponse(specs_json, content_type='application/json')

#Character
def char_list_all(request):
    return render(request, 'crud/char_index.html')

def ajax_char_list_all(request):
    chars = Character.objects.all().values('pk', 'name', 'specialization__name', 'life', 'mana', 'armor')
    chars_dict = ValuesQuerySetToDict(chars) #Tricky
    chars_json = json.dumps(chars_dict)

    return HttpResponse(chars_json, content_type='application/json')

def char_new(request):
    return render(request, 'crud/char_form.html')

def char_edit(request, char_id):
    # Receive id from char
    character = Character.objects.get(pk=char_id)
    return render(request, 'crud/char_form.html', { 'character' : character })

def char_save(request):
    pk = request.POST.get('pk', None)

    specialization_id = request.POST.get('specialization', None)
    specialization = Specialization.objects.get(pk=specialization_id)

    name = request.POST.get('name', None)
    life = request.POST.get('life', None)
    mana = request.POST.get('mana', None)
    armor = request.POST.get('armor', None)

    if pk is "": #Creating new
        character = Character(specialization=specialization, name=name, life=life, mana=mana, armor=armor)
    else: #Editing
        character = Character(pk=pk, specialization=specialization, name=name, life=life, mana=mana, armor=armor)

    character.save()
    return render(request, 'crud/char_index.html')

def char_delete(request):
    return render(request, 'crud/char_index.html')

def ajax_char_delete(request):
    id = request.POST.get('id', None)
    character = Character.objects.get(pk=id)
    character.delete()

    chars_json = serializers.serialize('json', Character.objects.all())
    return HttpResponse(chars_json, content_type='application/json')

#Utils methods
def ValuesQuerySetToDict(vqs): #Converting ValuesQuerySet to Dict, it allows to convert Dict to jSon after
    return [item for item in vqs]