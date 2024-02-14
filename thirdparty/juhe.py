# -*- coding: utf-8 -*-
import urllib
import urllib.request as request
import urllib.error as error
import json

headers = {"Content-Type": "application/x-www-form-urlencoded"}


# 天气预报查询示例
def weather(city):
    api_url = 'http://apis.juhe.cn/simpleWeather/query'
    params_dict = {
        "city": city,  # 查询天气的城市名称，如：北京、苏州、上海
        "key": '3f237673d0840d9e35723ddb232ce0ae',  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['error_code']
                if (error_code == 0):
                    temperature = result['result']['realtime']['temperature']
                    humidity = result['result']['realtime']['humidity']
                    info = result['result']['realtime']['info']
                    wid = result['result']['realtime']['wid']
                    direct = result['result']['realtime']['direct']
                    power = result['result']['realtime']['power']
                    aqi = result['result']['realtime']['aqi']
                    response = dict()
                    #response['当前城市'] = city
                    response['温度'] = temperature
                    response['湿度'] = humidity
                    response['天气'] = info
                    response['风向'] = direct
                    response['风力'] = power
                    response['空气质量'] = aqi
                    #print("当前城市：%s\n温度：%s\n湿度：%s\n天气：%s\n天气标识：%s\n风向：%s\n风力：%s\n空气质量：%s" % (
                    #    city, temperature, humidity, info, wid, direct, power, aqi))
                    return response
                else:
                    print("请求失败:%s %s" % (result['error_code'], result['reason']))
            except Exception as e:
                print("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            print("请求异常")
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        # 其他异常
        print(err)


#if __name__ == '__main__':
#    main()
