# coding:utf-8
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from ApiSoftware.loginApi.PublicParameters import meta_json_Response,_Response_public
from ApiSoftware.modes import login_models
from ApiSoftware.loginApi.PublicParameters import get_dates
import time,datetime
# @api_view(http_method_names=['post'])  #只允许post
# from rest_framework.decorators import api_view
import hashlib


class usr_login(APIView):


    def post(self,request):
        register_models = login_models

        parameter_json = request.body  # 取到request的body（data）
        parameter = json.loads(parameter_json)  # json转字典
        print(parameter)

        get_phone = 'phone'
        get_password = 'password'

        get_json_Response = meta_json_Response()
        get_Response_public = _Response_public()

        if get_phone in parameter and get_password in parameter:

            phone=parameter[get_phone]
            password=parameter[get_password]
            if phone and password:
                inspect_phone = register_models.tbl_user.objects.filter(phone__contains=phone,password__contains=password)
                if  inspect_phone:
                    inspect=True
                else:
                    inspect=False

                if inspect == True:
                    def _token_value(value):
                        hash = hashlib.sha256()
                        hash.update(value.encode('utf-8'))
                        return (hash.hexdigest())

                    nowTime_to_token = datetime.datetime.today()
                    nowTime_to_token=str(nowTime_to_token)
                    get_user_str=str(phone+password+nowTime_to_token)
                    get_token=_token_value(get_user_str)
                    inster_token = login_models.tbl_user.objects.filter(phone__contains=phone, password__contains=password)

                    user_get_list=[]
                    for value in inster_token:
                        value.token_value=get_token
                        # user_get_list.append(sql_user_)
                    # # for value  in user_get_list:
                    #     value.token_value=inster_token
                        value.save()
                    user_list = []
                    for users in inster_token:
                        name_info=[users.user_name,users.token_value]
                        user_list.append(name_info)
                    usersInfo=user_list[0]

                    datas = {
                        'status': 'true',
                        'message': '登录成功！',
                        'name':usersInfo[0],
                        'token':get_token

                    }
                    return HttpResponse(get_json_Response.json_Response(datas),
                                        content_type="application/json,charset=utf-8")

                else:
                    datas = {
                        'status': 'false',
                        'message': '手机号或密码不正确！',
                        'data': 'null'

                    }

                    return HttpResponse(get_json_Response.json_Response(datas),
                                        content_type="application/json,charset=utf-8")



            else:
                return HttpResponse(get_Response_public.InvalidParameter(),
                                    content_type="application/json,charset=utf-8")

        else:
            return HttpResponse(get_Response_public.InvalidParameter(), content_type="application/json,charset=utf-8")




