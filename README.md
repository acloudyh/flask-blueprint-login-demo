## 网关服务
### 安装依赖
```shell script
pip3 install -r requirements.txt
```

### 启动gateway项目
```shell script
gunicorn -w 1 -b 127.0.0.1:4444 manage:app
```
**说明**： `-w 或 --workers` 指定启动几个进程, `-b 或 --bind` 指定项目启动绑定域名和端口，


