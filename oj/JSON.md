# 题目结构Problem.struct
```javascript
[
    // 题目代码结构
    {
        "t": 0, // type; 0代表给定代码
        "s": true, // show; 显示文本是否与代码文本一致
        "c": "def plus(a,b):", // code; 用于组装最终代码的文本
        "d": "\t# 显示内容" // display; (仅在show=true时生效，若含有该关键字)用户看到的文本内容
    },
    // 填空区域
    {
        "t": 1, // type; 1代表填空区域
        "i": 0 // indentation; 该空位接收用户输入时的缩进量(tab数)
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