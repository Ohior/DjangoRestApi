#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-30 14:17:06
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-30 14:28:41
#  \\           //
#   \\         //
#


import requests

response = requests.get("http://127.0.0.1:8000/drinks/")
print(response.items())