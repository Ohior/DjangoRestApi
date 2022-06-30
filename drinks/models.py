#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-30 12:36:54
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-30 12:49:42
#  \\           //
#   \\         //
#

from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name