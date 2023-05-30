#### トークン化
--------------------------------------
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
文字列から演算子を取り出しトークン化

#### トークンデータの出力
--------------------------------------

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
入力された文字列を解析し、それぞれが、数値や演算子の情報を持つ、トークンデータのリストとして出力する


#### 計算を行う
--------------------------------------

```
priority_tokens = []
```
空のリストを作成し、後ほど、トークン列を格納していく

```
while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if len(priority_tokens) > 0 and priority_tokens[-1]['type'] in ['MULTI', 'DIVIDE']:
                operation = priority_tokens.pop() # 'multi'や'divideの演算子を取り出している
                if operation['type'] == 'MULTI':
                    priority_tokens[-1]['number'] *= tokens[index]['number'] # priority_tokensの最後の要素と、今の要素を計算する
                else:
                    priority_tokens[-1]['number'] /= tokens[index]['number']
            else:
                priority_tokens.append(tokens[index])
        else:
            priority_tokens.append(tokens[index])
        index += 1
 ```
 トークンを読み進めていき、もし数値トークンだったら最初のif文に入る<br>
 priority_tokensリストの最後の要素がMULTIかDIVIDEだった場合、その演算子を取り出し、operationに代入する<br>
 取り出した演算子に従い、演算を行う<br><br>
 
 もし、数値トークンでなかった場合（PLUSやMINUS）は、priority_tokensリストに格納しておく<br>
 すべての処理が終わったら、indexを隣に一つ進める<br>
 
 ```
 answer = priority_tokens[0]['number']
    index = 1
    while index < len(priority_tokens):
        if priority_tokens[index]['type'] == 'NUMBER':
            if priority_tokens[index - 1]['type'] == 'PLUS':
                answer += priority_tokens[index]['number']
            elif priority_tokens[index - 1]['type'] == 'MINUS':
                answer -= priority_tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1

    return answer
```
答えを格納するanswerを用意する<br>
answerには、priority_tokensの最初の数値トークンを代入する<br>

priority_tokensの長さ文ループを回し、それぞれの演算子に従って演算を行う


