# 使用的库

## py2exe
### 功能 ###
将脚本打包成EXE
### URL ###
http://www.py2exe.org/

## 解析Office ##
TODO

## GUI ##
### PyQT ###
https://riverbankcomputing.com/software/pyqt/intro
### kivy ###
http://kivy.org/#home

## 生成XML ##
mako

## ORM ##
### http://ponyorm.com/ ###
### https://github.com/coleifer/peewee ###
### https://docs.djangoproject.com/en/dev/topics/db/models/ ###

## 日志 ##
### URL ###
https://docs.python.org/2/library/logging.html

## 测试 ##
https://docs.python.org/2/library/unittest.html


# 打包Exe流程

## 将程序编译成EXE
-	cmd进入src所在目录
-	执行命令`pyinstaller main.py`
执行完毕之后生产目录 `/dist/main`

## 拷贝资源文件
将如下三个文件拷贝到`/dist/main`目录下面

    data.db
    input.xml
    images/

## 用ISS打包成安装包
-	将`打包安装程序.iss`拷贝到 `/dist/main`目录下面
-	编译安装程序
-	编译完成之后，可以通过build/Open Output Folder打开安装程序

## 注意
不要安装在C盘，可能会无法执行写数据库操作