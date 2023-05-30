#### トークン化
文字列から演算子を取り出しトークン化
```
def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1
```
```
def read_multi(line, index):
    token = {'type': 'MULTI'}
    return token, index + 1
```

#### トークンデータの出力
入力された文字列を解析し、それぞれが、数値や演算子の情報を持つ、トークンデータのリストとして出力する

```
def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multi(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens
```

