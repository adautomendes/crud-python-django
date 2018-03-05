# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Specialization(models.Model):
    name = models.CharField('Name', max_length=100,null=False,blank=False)
    initial_life = models.IntegerField('Initial Life')
    initial_mana = models.IntegerField('Initial Mana')

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        ordering = ['name']

    def __unicode__(self):
        return "%s" % (self.name)

class Character(models.Model):
    specialization = models.ForeignKey(Specialization,verbose_name='Specialization')
    name = models.CharField('Name', max_length=100,null=False,blank=False)
    life = models.IntegerField('Life')
    mana = models.IntegerField('Mana')
    armor = models.IntegerField('Armor')

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ['name']

    def __unicode__(self):
        return "%s - (%s)" % (self.name, self.specialization.name)