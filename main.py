
KEYWORD_DICT = {
    "(": "1",
    ")": "1",
    "AND": "1",
    "OR": "1",
    "NOT": "1",
}


def string_and_not_or(rules: str, content: str):
    # 替换中文括号
    rules = rules.replace('（', '(').replace('）', ')')
    _str = ''
    for x in rules:
        if x not in ['(', ')', ' ']:
            _str += x
        elif x == ' ':
            if KEYWORD_DICT.get(_str):
                _str = ''
            else:
                if _str in content:
                    rules = rules.replace(_str, '1', 1)
                else:
                    rules = rules.replace(_str, '0', 1)
                _str = ''

    if _str in content:
        rules = rules.replace(_str, '1', 1)
    else:
        rules = rules.replace(_str, '0', 1)
    return eval(rules.lower())


# 方法二：
def string_and_not_or_2(rules: str, content: str):
    # 替换中文括号
    rules = rules.replace('（', '(').replace('）', ')')
    rules_list = rules.split(' ')
    for x in rules_list:
        rep_x = x.replace('(', '').replace(')', '')
        if KEYWORD_DICT.get(rep_x):
            continue
        else:
            if rep_x in content:
                rules = rules.replace(x, '1', 1)
            else:
                rules = rules.replace(x, '0', 1)
    return eval(rules.lower())


if __name__ == '__main__':
    # 规则
    rules = '(尼哥 OR 黑人) AND (未进化完全 OR 猴子） AND NOT 是人'
    # 第二个字符串
    content = '测试后的字符串，黑人是人，不是未进化完全的猴子，富强民主文明和谐。'
    result = string_and_not_or(rules, content)
    print(result)
