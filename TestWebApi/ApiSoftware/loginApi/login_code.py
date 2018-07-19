# coding:utf-8
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from ApiSoftware.loginApi.PublicParameters import meta_json_Response,_Response_public
from ApiSoftware.modes import login_models
import random
from ApiSoftware.loginApi.PublicParameters import get_dates
from ApiSoftware.loginApi import SendEmail


class cx_sendCode(APIView):

    def post(self,request):
        # sendCode=login_models.tbl_verCode
        register_models = login_models
        time_get=get_dates()

        code_list = []
        for i in range(1, 9):
            code = random.choice('abcdefghijklmnopqrstuvwxyz!ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            code_list.append(code)
        user_code = "".join(str(i) for i in code_list)

        get_pthon='phone'
        get_email='email'
        # get_code='code'
        # get_effective_time='effective_time'

        parameter_json = request.body  # 取到request的body（data）
        parameter = json.loads(parameter_json)  # json转字典
        get_json_Response = meta_json_Response()
        get_Response_public = _Response_public()

        if get_pthon in parameter and get_email in parameter:
            phone=parameter['phone']
            email = parameter['email']
            # code = parameter['code']
            #当前时间
            nowTime=time_get.get_nowTime()
            #五分钟后时间
            laterTime=time_get.get_laterTime()


            if phone and email:
                email_str1='@'
                email_str2 = '.com'
                email_str3 = '.top'
                if email_str1 in email and email_str2 in email or email_str1 in email and email_str3 in email:
                    email_send=SendEmail.SendEmail()
                    Result_Email=email_send.sendEmailForUsr(user_code,email)
                    if Result_Email==True:
                        code_res = register_models.tbl_verCode(email=email, phone=phone,code=user_code,creat_time=nowTime,effective_time=laterTime,
                                                                status='1')
                        code_res.save()

                        datas = {
                            'status': 'true',
                            'message': '验证码发送成功！',
                            'email': email

                        }
                        return HttpResponse(get_json_Response.json_Response(datas),content_type="application/json,charset=utf-8")
                    else:
                        datas = {
                            'status': 'false',
                            'message': '验证码发送失败，请检查邮箱填写是否正确！'
                        }


                        return HttpResponse(get_json_Response.json_Response(datas),content_type="application/json,charset=utf-8")

                else:
                    datas = {
                        'status': 'false',
                        'message': '请检查邮箱填写是否正确！'
                    }

                    return HttpResponse(get_json_Response.json_Response(datas),
                                        content_type="application/json,charset=utf-8")

            else:
                return HttpResponse(get_Response_public.InvalidParameter(),content_type="application/json,charset=utf-8")



        else:
            return HttpResponse(get_Response_public.InvalidParameter(), content_type="application/json,charset=utf-8")






