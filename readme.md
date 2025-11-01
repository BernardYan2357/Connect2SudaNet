# Connect2SudaNet

用于自动化登录苏州大学校园网的python程序

参考：[(理论上)各大高校都适用的全平台校园网自动登录实现方法](https://www.bilibili.com/opus/646733491161006112)

## 下载

请点击`Releases`一栏

## 使用

打开目录下的config.json，填写以下内容

- "user_number": "填写你的学号",
- "user_password": "填写你的密码",
- "operator": "填写运营商代码,移动cmcc,联通cucc,电信ctcc"

实际使用时只需点击执行，查看右下角弹窗显示的登录状态，如果看不见右下角弹窗通知，请查看是否开启了请勿打扰，也可点开通知栏查看登录状态

## 环境要求

仅在windows11系统，python=3.13上测试过，其他windows，python版本可能可以运行，但是通知栏图标显示可能不正常

本人能力有限，可能有诸多bug，欢迎提issue
