# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : mqtt_server.py
# Software: PyCharm
# Time    : 2020/3/27 11:00
# Description:
import sys

import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 1883
TOPIC = "mytopic"


def client_loop():
    client = mqtt.Client()  # ClientId不能重复，所以使用当前时间
    server_connect(client)


def server_connect(client):
    client.on_connect = on_connect  # 启动订阅模式
    client.on_message = on_message  # 接收消息
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def server_stop(client):
    client.loop_stop()  # 停止服务端
    sys.exit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    """
    接收客户端的消息
    :param client: 连接信息
    :param userdata:
    :param msg: 客户端返回的消息
    """
    print("Start server!")
    print("topic:[{}],接收的消息:[{}]".format(msg.topic, msg.payload.decode("utf-8")))


if __name__ == '__main__':
    client_loop()
