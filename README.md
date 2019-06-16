# PyFillin OJ
基于Django的python代码填空评测系统

# Features
## Django功能
* ### 用户系统usr_sys
    * 登录/注册/登出
    * 学号邮箱验证
    * 修改密码
    * 学号邮箱找回密码
    * 昵称+[Gravatar](https://www.gravatar.com)头像

## 辅助工具
* ### [出题工具](tools/gen_problem.html)
    * 插入代码块与用户填空内容
    * 导出与读取JSON结构
    * 预览用户视角与组装测评代码

# TODO

## 基础设施

### 代码结构组装器
通过读取Problem的代码结构与Submission的提交结构  
获得用户最终需运行的代码
#### 额外功能:
1. 自动缩进转换(填空块缩进、tab与space互转，等)
1. AST代码检查<br>*可从[代码竞技场](https://github.com/YukkuriC/django_ai_arena)移植*

### 代码运行器
可通过命令行调用的代码运行设施(**与Django环境隔离**)  
通过命令行参数或stdin接收组装完成的代码与多组测试点  
自动进行计时、判题等操作，并输出判题结果
#### Django侧对接功能:
1. 进程监控+stdout连接+数据库读写接口
1. 限制单用户发起提交频率

### 错误提示系统
通过读取用户提交的错误进行建议  
与前端设施配合显示
#### 额外功能:
1. 根据traceback确认具体的报错行数
1. 综合助教人工与所有提交统计的智能提示

# CHANGELOG
## 20190617
* 确定题目JSON结构
* 开发了出题工具

## 20190616
* 创建了必需的ORM模型

## 20190615
* 自[代码竞技场](https://github.com/YukkuriC/django_ai_arena)移植用户系统
* 创建文档

## 20190614
* 立项