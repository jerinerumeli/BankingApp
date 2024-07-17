from django.http import JsonResponse
from rest_framework import status
from .serializer import userSerializer
from .serializer import authSerializer
from .serializer import accountSerializer
from .models import authCredentials
from .models import userAccount
from .models import createUser
from BankingApp.settings import encyption_key
from BankingApp.settings import algorithm
import jwt
import datetime

#------token checking---------#
def validatetoken(request):
        try:
            gettoken = request.headers["Authorization"][7:]
            entoken = jwt.decode(gettoken,encyption_key,algorithms=algorithm)
            authtoken = (authCredentials.objects.get(id=entoken["id"])).token
            if (gettoken==authtoken):
                return True
            else:
                return False
        except:
            return False
#-----------------#

#--------authsignin------#

def auth(request):
    try:
        if request.data:
            print(request.data,"yyyyyyyyyyyyyyyyyyyyy")#
            serializer = authSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                auth_obj = authCredentials.objects.get(emailid=request.data["emailid"])
                return JsonResponse({"msg":"successully registered","id":auth_obj.id,"status":"200"},status=status.HTTP_200_OK)
            return JsonResponse({"msg" : "failed..","status":"406"})
    except:
       return JsonResponse({"msg" : "failed","status":"406"})
    
#-------------#

#---------------signin-------#
def add_user(request,pk):
    try:
        if request.data:
            serializer = userSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # account_obj = userAccount.objects.get(mobile=request.data["mobile"])
                user_obj = createUser.objects.get(mobile=request.data["mobile"])
                user_obj.auth = authCredentials.objects.get(id=pk)
                user_obj.save()
                return JsonResponse({"msg" : "successfully created new user","status":"201"})
        return JsonResponse({"msg" : "give valid user details valid or try different user details","status":"406"})
    except:
        return JsonResponse({"msg" : "failed","status":"406"})
#----------------#

#--------------login-----------#
def user_login(request):
    try:
        if request.data:
            try:
                emailid = request.data["emailid"]
                password = request.data["password"]
                authinstance = authCredentials.objects.get(emailid=emailid,password=password)
                payload = {
                    "id":authinstance.id,
                    "emailid":authinstance.emailid,
                    # "name":authinstance.name,
                    "timestamp":authinstance.timestamp
                }
                token = jwt.encode(payload,encyption_key,algorithm=algorithm)
                authinstance.token = token
                authinstance.timestamp = (datetime.datetime.now()).timestamp()
                authinstance.save()
                return JsonResponse({"msg":authinstance.emailid+" is successfully logined","token":authinstance.token,"status":"200"})
            except:
                return JsonResponse({"msg":"emailid or password is incorrect..!","status":"406"})
    except:
        return JsonResponse({"msg" : "failed","status":"406"})

#------------#

#--------------transaction--------#
# def user_transaction(request,pk):
#     try:
#         if request.data:
#             type = request.data["type"]
#             serializer = accountSerializer(data=request.data)
#             transaction_obj = userAccount.objects.get(account_number=request.data["account_number"])#ivide thetti
#             if (type=="Credited"):
#                 if serializer.is_valid():
#                     serializer.save()
#                     transaction_obj.account = authCredentials.objects.get(id=pk)
#                     transaction_obj.save()
#                     return JsonResponse({"msg" : "successfully saved transaction","status":"200"},status=status.HTTP_200_OK)
                
#             elif (type=="Debited"):
#                 auth_obj = authCredentials.objects.get(id=transaction_obj.account.id)
#                 balance = auth_obj.account.balance
#                 if(request.transaction>=balance):
#                     if serializer.is_valid():
#                         serializer.save()
#                         balance=balance-request.transaction
#                         auth_obj.account.balance = balance
#                 else:
#                     return JsonResponse({"msg" : "insuffitent balance","status":"406"})
#         return JsonResponse({"msg" : "give valid user details valid or try different vendor code","status":"406"})
#     except:
#         return JsonResponse({"msg" : "failed","status":"406"})
#---------------#