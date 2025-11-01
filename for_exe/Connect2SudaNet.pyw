# -*- coding: utf-8 -*-
#参考教程：https://www.bilibili.com/opus/646733491161006112
# 适用于苏州大学校园网登录

from win11toast import toast
from urllib.parse import quote
import requests
import socket
import os
import sys
import json

def load_config():
    config_path = os.path.join(os.path.dirname(sys.executable if hasattr(sys, 'frozen') else __file__), 'config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

def main():
    # 独立参数
    config = load_config()
    user_number = config['user_number']
    user_password = config['user_password']
    operator = config['operator'] # cucc 联通，cmcc 移动，ctcc 电信

    # 账号格式化
    user_account = f',b,{user_number}@{operator}'
    encoded_user_account = quote(user_account)

    current_ip = get_local_ip()
    login_IP = 'http://10.9.1.3'
    result_return = '"result":"1"'

    sign_url = (
        'http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1'
        f'&user_account={encoded_user_account}&user_password={user_password}'
        f'&wlan_user_ip={current_ip}&wlan_user_ipv6=&wlan_user_mac=000000000000'
        f'&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=10052'
    ) #在 Python 中，使用括号 () 包裹的多行字符串拼接，不会在字符串中插入换行符

    signed_in_title = '注销页'
    not_sign_in_title = '上网登录页'

    already_icon = resource_path('res/Tips.ico')
    success_icon = resource_path('res/Check.ico')
    false_icon = resource_path('res/Cross.ico')
    unknown_icon = resource_path('res/Questionmark.ico')

    # 检查是否已登录
    try:
        r = requests.get(login_IP, timeout=3)
        req = r.text
    except Exception as e:
        toast('网络异常', str(e), icon=unknown_icon, duration='short')
        sys.exit(1)

    if signed_in_title in req:
        toast('该设备已经登录', '校园网状态', icon=already_icon, duration='short')
        sys.exit(0)

    elif not_sign_in_title in req:
        try:
            r = requests.get(sign_url, timeout=3)
            req = r.text
        except Exception as e:
            toast('登录请求失败', str(e), icon=false_icon, duration='short')
            sys.exit(1)
        if result_return in req:
            toast('登录成功', '校园网状态', icon=success_icon, duration='short')
        else:
            toast('登录失败', '校园网状态', icon=false_icon, duration='short')
        sys.exit(0)

    else:
        toast('未连接到校园网', '校园网状态', icon=unknown_icon, duration='short')
        sys.exit(0)

if __name__ == "__main__":
    main()