import ast


def construct_code(problem, fillins):
    """ 从问题结构与用户输入组装成测试代码 """
    tmp, ind = [], 0
    for struct in problem:
        if struct['t'] == 0:  # 题目代码结构
            tmp.append(struct['c'])
        elif ind < len(fillins):  # 填空逐行缩进
            for line in fillins[ind].split('\n'):
                tmp.append('\t' * struct['i'] + line)
            ind += 1
    return '\n'.join(tmp)


class CodeChecker:
    _import_whitelist = [
        'math', 'random', 'copy', 'numpy', 'time', 'collections', 'itertools',
        'functools', 'datetime'
    ]  # 允许使用的库
    _func_blacklist = ['eval', 'exec', 'compile', '__import__',
                       'open']  # 禁止使用的函数
    _ast_errors = ['非法import', '非法函数调用']

    @classmethod
    def _invalid_import(cls, module):
        tmp = module.split('.')[0]
        return tmp not in cls._import_whitelist

    @classmethod
    def _ast_errormsg(cls, node, info, content):
        text = '第%s行 %s: %s' % (node.lineno, cls._ast_errors[info], content)
        return AssertionError(text)

    @classmethod
    def construct_ast(cls, code_raw):
        """
        将代码文本转换为AST，并检查模块使用与代码规范等
        返回元组: (AST, 检查警告列表)
        """
        warnings = []

        # 将待导入代码转换为AST
        code_tree = ast.parse(code_raw, '<code>')

        # 检查非法import与函数
        for node in ast.walk(code_tree):
            if isinstance(node, ast.Import):
                for module in node.names:
                    if cls._invalid_import(module.name):
                        raise cls._ast_errormsg(node, 0, module.name)
            if isinstance(node, ast.ImportFrom):
                if cls._invalid_import(node.module):
                    raise cls._ast_errormsg(node, 0, node.module)
                elif node.names[0].name == '*':
                    warnings.append('第%s行 请写明import内容' % node.lineno)
            if isinstance(node, ast.Call):
                func = node.func
                func_name = getattr(func, 'attr', getattr(func, 'id', None))
                if func_name in cls._func_blacklist:
                    raise cls._ast_errormsg(node, 1, func_name)

        # 返回AST
        return code_tree, warnings


if __name__ == '__main__':
    import json
    prob = json.loads(
        '''[{"t":0,"s":true,"c":"# 给定列表lst, 请反转列表内部的所有元素\ndef revert(lst):"},{"t":1,"i":1},{"t":0,"s":false,"c":"lst=list(map(int,input().split()))\nrevert(lst)\nprint(*lst,sep=' ')"}]''',
        strict=0)
    usr_input = [
        "tmp=lst[::-1]\nlst.clear()\nlst.extend(tmp)\nfrom math import *",
    ]
    code = construct_code(prob, usr_input)
    print(code)
    tree, warn = CodeChecker.construct_ast(code)
    print(warn)