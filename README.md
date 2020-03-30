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


## 命名规范

• 包名：全部小写字母，中间可以由点分隔开，不推荐使用下画线。作为命名空间，包名应该具有唯一性，推荐采用公司或组织域名的倒置，如com.apple.quicktime.v2。
• 模块名：全部小写字母，如果是多个单词构成，可以用下画线隔开，如dummy_threading。
• 类名：采用大驼峰法命名③，如SplitView。
• 异常名：异常属于类，命名同类命名，但应该使用Error作为后缀。如FileNotFoundError。
• 变量名：全部小写字母，如果由多个单词构成，可以用下画线隔开。如果变量应用于模块或函数内部，则变量名可以由单下画线开头；变量类内部私有使用变量名可以双下画线开头。不要命名双下画线开头和结尾的变量，这是Python保留的。另外，避免使用小写L、大写O和大写I作为变量名。
• 函数名和方法名：命名同变量命名，如balance_account、_push_cm_exit。
• 常量名：全部大写字母，如果是由多个单词构成，可以用下画线隔开，如YEAR和WEEK_OF_MONTH


