import re
content = """
    寻隐者12345@qq.com不遇
    朝代：唐asdf12dsa#abc.com代
    作python666@163.cn者：贾岛
    松下问童子，言师python-adc@163.com采药去。
    只在python-ant-666@sina.net此山中，云深不知处。
"""
pattern = re.compile("""
    [a-zA-Z0-9_-]+   #+代表前的字符至少出现一次，
    @
    [a-zA-Z0-9]+
    \.
    [a-zA-Z]{2,4}
""", re.VERBOSE)
results = pattern.findall(content)

for result in results:
    print(result)
