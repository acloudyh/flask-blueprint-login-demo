# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : mqtt_server.py
# Software: PyCharm
# Time    : 2020/3/27 11:00
# Description:
import time

import paho.mqtt.client as mqtt

from app import config

HOST = "127.0.0.1"
PORT = 1883
TOPIC = "mytopic"  # 客户端发布消息topic

CLIENT_ID = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
"""
client_id是连接到代理。如果client_id的长度为零或为零，则行为为由使用的协议版本定义。如果使用MQTT v3.1.1，
那么一个零长度的客户机id将被发送到代理，代理将被发送为客户端生成一个随机变量。如果使用MQTT v3.1，那么id将是
随机生成的。在这两种情况下，clean_session都必须为True。如果这在这种情况下不会产生ValueError。
注意：一般情况下如果客户端服务端启用两个监听那么客户端client_id 不能与服务器相同，如这里用时间"20190222142358"作为它的id，
如果与服务器id相同，则无法接收到消息
"""


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))


if __name__ == '__main__':

    client = mqtt.Client(CLIENT_ID)  # ClientId不能重复，所以使用当前时间
    client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.publish(TOPIC, "你好 MQTT", qos=0, retain=False)  # 发布消息

    # publish.single("test", "你好 MQTT", qos=1, hostname=HOST, port=PORT, client_id=client_id,
    #                auth={'username': "admin", 'password': "123456"})
