#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-30 12:52:52
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-30 12:59:49
#  \\           //
#   \\         //
#

# serializers convert Python/ data to json

from rest_framework import serializers

from .models import Drinks

class DrinkSerializers(serializers.ModelSerializer):
    # meta class describing the model
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'description',]