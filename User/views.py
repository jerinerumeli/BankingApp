from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import viewsfunction as vf
# Create your views here.

# class userCreation(APIView):
#     def post(self,request,pk):
#         if vf.validatetoken(request):
#             try:
#                 return vf.add_user(request,pk)
#             except Exception as e:
#                     return JsonResponse({"error_msg": e})            
#         else:
#             return JsonResponse({"msg":"NO authorization"})        

@api_view(["POST"])
def login(request):
    try:
        return vf.user_login(request)
    except Exception as e:
            return JsonResponse({"error_msg": e})            


@api_view(["POST"])
def authin(request):
    try:
        return vf.auth(request)
    except Exception as e:
            return JsonResponse({"error_msg": e})            

    
@api_view(["POST"])
def signin(request,pk):
    try:
        return vf.add_user(request,pk)
    except Exception as e:
            return JsonResponse({"error_msg": e})            

    

# @api_view(["POST"])
# def transaction(request):    
#     if vf.validatetoken(request):
#             try:
#                 return vf.user_transaction(request)
#             except Exception as e:
#                     return JsonResponse({"error_msg": e})            
#     else:
#         return JsonResponse({"msg":"NO authorization"})