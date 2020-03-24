## 网关服务

### 安装pip3
```shell script
apt install python3-pip
```

### 安装依赖
```shell script
pip3 install -r requirements.txt
```

### 启动gateway项目
```shell script
gunicorn -w 1 -b 127.0.0.1:9999 manage:app
```
**说明**： `-w 或 --workers` 指定启动几个进程, `-b 或 --bind` 指定项目启动绑定域名和端口，


```python
# backupCount 备份日志个数; maxBytes 单个文件大小
file_handler = RotatingFileHandler(os.path.join(log_path, log_name), maxBytes=10 * 1024 * 1024, backupCount=10, encoding='UTF-8')

# 日志打印
current_app.logger.info()

# sqlite存放路径
# //// 绝对路径
# ///  相对路径
# SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/neo/code/sqlite3flask.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///./sqlite3flask.db'
```


