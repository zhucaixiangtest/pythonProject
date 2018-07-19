import json
import time
import datetime


from ApiSoftware.modes import login_models


class meta_json_Response():

    test= login_models

    def json_Response(self,rest_dict):
      rest=dict(rest_dict)

      rest=json.dumps(rest,ensure_ascii=False)
      return rest


# 公共参数类
class _Response_public(meta_json_Response):

   # def __init__(self):
   #   self.Success='0'
   #
   #   self.fails='1'


  # 返回无效参数
   def InvalidParameter(self):

    dict_InvalidParameter={

      'status':'false',
      'message':'无效参数',
      'data':'null'

    }
    json_InvalidParameter=self.json_Response(dict_InvalidParameter)

    return json_InvalidParameter

class get_dates():


    def get_laterTime(self):
        # 获取五分钟后时间
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t = time.localtime(time.time() + 300)

        #
        laterTime = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return laterTime


     # 获取当前时间
    def get_nowTime(seif):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return nowTime

    # 比较当前时间和数据库存的有效期
    def ComparisonTime(self,sql_time):
        nowTime = datetime.datetime.today()
        new_time = nowTime.strftime('%Y-%m-%d %H-%M-%S')
        print(type(new_time))
        _time = new_time.replace('-', '')
        _null_time = _time.replace(' ', '')
        nowTime = eval(_null_time)

        if sql_time:
            sql_times = sql_time.strftime('%Y-%m-%d %H-%M-%S')
            sql_time = sql_times.replace('-', '')
            sql_null_time = sql_time.replace(' ', '')
            sql_time = eval(sql_null_time)

            if sql_time > nowTime:
                return True
            else:
                return False
        else:
            return False













