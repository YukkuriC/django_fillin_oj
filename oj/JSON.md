# 题目结构Problem.struct
```javascript
[
    // 题目代码结构
    {
        "type": "struct",
        "show": true, // 显示文本是否与代码文本一致
        "code": "def plus(a,b):", // 用于组装最终代码的文本
        "display": "\t# 显示内容" // (仅在show=true时生效，若含有该关键字)用户看到的文本内容
    },
    // 填空区域
    {
        "type": "fillin",
        "indent": 0 // 该空位接收用户输入时的缩进量(tab数)
    }
]
```

# 提交内容Submission.content
```javascript
[
    "", // 按顺序获取题目结构每个填空区域内容
]
```

# 评测结果Submission.detail
```json
```