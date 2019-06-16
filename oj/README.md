## 模型

### 题目Problem
域|名称|格式|需求
-|-|-|-
title|题目|文本|问题标题
descrip|题目描述|文本或JSON|对题目需求的描述、范例输入输出等
struct|代码结构|JSON|定义填空题每空的位置、缩进等<br>完全自由编写的题目留空

### 测试点TestCase
域|名称|格式|需求
-|-|-|-
problem|题目|外键|测试点对应的题目
index|编号|int或str|该测试点名称
time_limit|时间限制|float|测试点最大用时
stdin|输入|文本|1. stdin<br>2. 序列化的python对象
stdout|输出|文本|1. stdout<br>2. 序列化的python对象<br>3. 序列化的判题函数

### 用户提交Submission
域|名称|格式|需求
-|-|-|-
user|用户|外键|发起提交的用户
problem|题目|外键|提交对应的题目
time|提交时间|datetime|提交发起时间
content|提交内容|JSON|前端组装的填空内容
status|状态|int|Running/Accepted/xxxError
time|用时|int|总用时(毫秒数)
detail|细节|JSON|(若通过)测试点详细用时<br>(若未通过)错误测试点的细节