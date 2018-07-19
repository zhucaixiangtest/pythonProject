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

class cx_register(APIView):

    #register api

    def post(self,request):
            # jsons=PublicParameters
            register_models= login_models

            parameter_json = request.body    #取到request的body（data）
            parameter=json.loads(parameter_json)  #json转字典

            get_name = 'name'
            get_phone = 'phone'
            get_password = 'password'
            get_email = 'email'
            get_code = 'code'

            get_json_Response = meta_json_Response()
            get_Response_public=_Response_public()

            if get_name in parameter and get_phone in parameter and get_password in parameter and get_email in parameter and get_code in parameter:

               #body需要传name,phone,paw,email
                name = parameter[get_name]
                phone = parameter[get_phone]
                password = parameter[get_password]
                email = parameter[get_email]
                code = parameter[get_code]

                if name and phone and password and email and code:

                            inspect_phone=register_models.tbl_user.objects.filter(phone__contains=phone)
                            if inspect_phone:
                                inspect=True
                            else:
                                inspect=False

                            phone_list=[]

                            if inspect==True:
                                for phones in inspect_phone:
                                    get_phones=phones.phone
                                    phone_list.append(get_phones)

                                if phone in phone_list:
                                    datas = {
                                        'status': 'false',
                                        'message': '该手机号已注册！',
                                        'data': 'null'

                                    }

                                    return HttpResponse(get_json_Response.json_Response(datas),content_type="application/json,charset=utf-8")

                            elif inspect==False or phone not in phone_list :

                                inspect_code = register_models.tbl_verCode.objects.filter(email__contains=email,code__contains=code,phone__contains=phone)
                                code_list=[]
                                if inspect_code:
                                      inspectcode=True
                                else:
                                      inspectcode=False

                                if inspectcode==True :
                                    for codes in inspect_code:
                                        get_email_code=[codes.email,codes.code,codes.effective_time]
                                        code_list.append(get_email_code)

                                    for fortime in code_list:
                                        usr_request = [email, code]
                                        get_sql_time=[fortime[0],fortime[1]]
                                        get_time=fortime[2]
                                        false_be_true=get_dates().ComparisonTime(get_time)
                                        print(false_be_true)


                                        # times=(get_time-get_time_class).total_seconds()
                                        # print(times)
                                        if usr_request == get_sql_time and false_be_true == True:

                                            register_res = register_models.tbl_user(user_name=name, email=email, phone=phone, password=password,
                                                                                    status='1')  # 传值不为空，插入到user表
                                            register_res.save()

                                            datas = {
                                                'status': 'true',
                                                'message': '注册成功！',
                                                'name': name,
                                                'phone':phone

                                            }

                                            return HttpResponse(get_json_Response.json_Response(datas), content_type="application/json,charset=utf-8")

                                        elif false_be_true == False:
                                            datas = {
                                                'status': 'false',
                                                'message': '验证码已过期！',
                                                'data': 'null'

                                            }

                                            return HttpResponse(json.dumps(datas),
                                                            content_type="application/json,charset=utf-8")


                                        else:
                                            return HttpResponse(json.dumps({'status': 'false',"message": "未知错误"}),
                                                            content_type="application/json,charset=utf-8")

                                else:
                                    return HttpResponse(json.dumps({'status': 'false',"message": "验证码和邮箱不匹配"}),
                                                        content_type="application/json,charset=utf-8")


                else:
                    return HttpResponse(get_Response_public.InvalidParameter(),content_type="application/json,charset=utf-8")
            else:
                return HttpResponse(get_Response_public.InvalidParameter(), content_type="application/json,charset=utf-8")

