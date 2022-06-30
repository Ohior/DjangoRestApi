#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-30 12:57:46
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-30 14:15:13
#  \\           //
#   \\         //
#

from django.http import JsonResponse
from .serializers import DrinkSerializers
from .models import Drinks
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):#this is a get request, to make it a post request add a decorator above the function
    # format is added to parameters to convert to pure json
    if(request.method == 'GET'):#get from database
        # get all the drink
        drinks = Drinks.objects.all()
        # serialize them
        serializer = DrinkSerializers(drinks, many=True)
        # return data
        return Response(serializer.data)
    elif(request.method == 'POST'):#post to database
        serializer = DrinkSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE',])#get, update, delete from database
def drink_detail(request, id, format=None):
    # format is added to parameters to convert to pure json
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method == 'GET'):
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    elif(request.method == 'PUT'):
        serializer = DrinkSerializers(drink, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)