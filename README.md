基于django的图书管理系统
---------------

### 一、概要


欢迎您使用该图书管理系统，希望在您使用的过程中体验到便捷和愉快的使用感受，并对我们的软件提出您发现的问题和建议，谢谢。
联系邮箱：liangshuo1994@outlook.com

**注意事项：**
1、相关文件说明：
    flow.png          项目流程图
    tree.txt          该项目的所有文件
    requirements.txt  依赖包文件
    img-floder        项目效果图

2、环境安装：
    请您在python官网下载python3.5以上版本进行安装。

3、当前程序的所有依赖包及其精确版本号。
    请您打开CMD控制台，到依赖包同目录下，执行：pip install -r requirements.txt

4、测试用例文档给您提供了更好的测试思路，您可以通过测试用例达到更好的测试效果

5、该项目博客地址:
    http://www.cnblogs.com/venicid/p/9286796.html

6、github地址：
    https://github.com/venicid/BMS

	
### 二、需求与功能

1、需求
    1) 列出图书列表、出版社列表、作者列表
    2) 点击作者，会列出其出版的图书列表
    3) 点击出版社，会列出其下的图书列表
    4) 可以创建、修改、删除 图书、作者、出版社

2、功能实现概述
    login_reg模块
        1) 主页
            /
        2) 注册
            /reg/
        3) 登录
            /login/
        4) 注销
            /logout/

    book模块
        1)图书主页
            /book/index/
        2)图书操作
            /book/book_list/        # 图书list
            /book/add_book/         # 添加图书
            /book/edit_book/30/     # 编辑图书
            /delete_book/30/        # 删除图书
        3)作者操作
            /book/author_list/       # 作者list
            /book/add_author/        # 添加作者
            /book/edit_author/15/    # 编辑作者
            /book/delete_author/15/  # 删除作者
            /book/author2book/15/    # 查看该作者出版过的所有图书
        4)出版社操作
            /book/publish_list/       # 出版社list
            /book/add_publish/        # 添加出版社
            /book/edit_publish/16/    # 编辑出版社
            /book/delete_publish/16/  # 删除出版社
            /book/publish2book/16/    # 查看该出版社出版过的所有图书

    404错误
            /^.*/       # url not found


			
### 三、所用技术概述

1、验证用户是否登录：用户认证组件
	实质：session会话跟踪技术
	from django.contrib import auth
	通过中间件auth_middleware.py,采用白名单，对url进行控制，替代装饰器@login_requierd，否则每一个函数都有要加装饰器。
	from django.utils.deprecation import MiddlewareMixin

2、验证字段：表单forms组件	
	对每个数据库中的字段进行校验，返回error
	from django import forms 
		
3、自定义分页器
	分页器Paginator.py
	解耦
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

4、记录日志log
	settings配置文件，终端打印sql语句
	mylog.py 日志文件，解耦，终端打印并在log文件记录用户操作
	import logging
	
5、模板继承
	{% extends 'base.html' %}

	{% block site-header %}
    {% endblock %}

	
6、ORM表关系
	一对一(author authordetail)
		删除author，对应删除authordetail表的信息

	一对多(book publish)
		删除出版社,关联删除出版过的所有的本书

	多对多(book author)
		删除author，不会删除该作者出版过的书


7、注意点：
	1) 时区：
	settings.py配置
		# TIME_ZONE = 'UTC'
		TIME_ZONE = 'Asia/Shanghai'

	2) 静态文件目录
	STATICFILES_DIRS = [
		os.path.join(BASE_DIR, 'static')
	]
	
 

### 四、鸣谢

感谢在开发过程中的老师和同学们的帮助。
