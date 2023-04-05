import re
content = """
白日依19989881888山尽，黄河入456455468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""

pattern = r"(1[3-9])\d{9}"  # 中括号的意思是包含。d{9}表示9个字符长度。
print(re.sub(pattern, r"\1******", content))