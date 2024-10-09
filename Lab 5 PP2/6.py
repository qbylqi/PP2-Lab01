import re

def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]', ':', s)

# Пример
print(replace_space_comma_dot("Hello, world. It's nice."))  # 'Hello: world: It's nice:'
