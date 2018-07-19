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



class ModeifyPassword(APIView):

    def post(self,request):
        parameter_json = request.body  # 取到request的body（data）
        parameter = json.loads(parameter_json)  # json转字典

        get_phone='phone'
        get_email='email'
        get_code='code'
        get_new_pwd='newpassword'

        register_models = login_models
        get_json_Response = meta_json_Response()
        get_Response_public = _Response_public()

        if get_email in parameter and get_phone in parameter and get_code in parameter and get_new_pwd in parameter:
            phone=parameter[get_phone]
            code=parameter[get_code]
            email=parameter[get_email]
            password=parameter[get_new_pwd]

            if get_phone and get_email and get_code and password:
                inspect_phone_email = register_models.tbl_user.objects.filter(phone__contains=phone,email__contains=email)
                if inspect_phone_email:
                    inspect=True
                else:
                    inspect=False
                phone_email_list=[]
                if inspect==True:
                    for phone_emails in inspect_phone_email:
                        get_phones = [phone_emails.phone,phone_emails.email]
                        phone_email_list.append(get_phones)

                        usr_request=[phone,email]
                        if usr_request in phone_email_list:
                            inspect_code = register_models.tbl_verCode.objects.filter(email__contains=email,
                                                                                      code__contains=code,
                                                                                    phone__contains=phone)

                            if inspect_code:
                                inspectcode=True

                            else:
                                inspectcode=False

                            code_list=[]
                            if inspectcode==True:
                                for codes in inspect_code:
                                   get_email_code = [codes.phone,codes.email, codes.code, codes.effective_time]
                                   code_list.append(get_email_code)

                                for fortime in code_list:
                                    usr_request = [phone,email, code]
                                    get_sql_time = [fortime[0], fortime[1],fortime[2]]
                                    get_time = fortime[3]
                                    false_be_true = get_dates().ComparisonTime(get_time)
                                    # print(false_be_true)
                                    if usr_request == get_sql_time and false_be_true == True:
                                        update_pwd=login_models.tbl_user.objects.filter(phone__contains=phone,email__contains=email)
                                        update_list=[]
                                        for up_value in update_pwd:
                                            update_list.append(up_value)
                                        for value_get in update_list:
                                            value_get.password=password
                                            value_get.save()
                                            return HttpResponse(json.dumps({"status": "true", "message": "密码修改成功!"}),
                                                                content_type="application/json,charset=utf-8")


                                    else:
                                        return HttpResponse(json.dumps({"status":"false","message":"验证码无效或已过期!"}),
                                                            content_type="application/json,charset=utf-8")

                            else:
                                return HttpResponse(json.dumps({"status": "false", "message": "用户信息和验证码不匹配!"}),
                                                    content_type="application/json,charset=utf-8")


                        else:
                            return HttpResponse(json.dumps({"status": "false", "message": "用户信息不存在或填写有误!"}),
                                                content_type="application/json,charset=utf-8")
                else:
                    return HttpResponse(json.dumps({"status": "false", "message": "用户信息不存在或填写有误!"}),
                                        content_type="application/json,charset=utf-8")

            else:
                return HttpResponse(get_Response_public.InvalidParameter(),
                                    content_type="application/json,charset=utf-8")


        else:
            return HttpResponse(get_Response_public.InvalidParameter(), content_type="application/json,charset=utf-8")


