### mudularized_bracket_calculator.py
--------------------

#### evaluate関数でそれぞれの関数を呼び出す
```
def evaluate(tokens):
    tokens = evaluate_function(tokens)
    tokens = evaluate_brackets(tokens)
    tokens = evaluate_mul_div(tokens)
    return evaluate_plus_minus(tokens)
 ```
 
 #### 足し算引き算を評価する
 ```
 # calculate plus and minus
def evaluate_plus_minus(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    answer = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer
 ```
 トークンの長さ分ループを回し、<br>
 もし、トークンが数字だったら演算子の計算を行う<br>
 最後に計算結果を返す<br>
 evaluate_plus_minus関数は、evaluate関数内で最後に呼び出される<br>
 
 #### 割り算引き算を評価する
 ```
 # calculate multi and divide
def evaluate_mul_div(tokens):
    index = 1
    while index < len(tokens) - 1:
        if tokens[index]['type'] in ['MULTI', 'DIVIDE']:
            if tokens[index + 1]['type'] == 'NUMBER':
                if tokens[index]['type'] == 'MULTI':
                    tokens[index - 1]['number'] *= tokens[index + 1]['number']
                elif tokens[index]['type'] == 'DIVIDE':
                    tokens[index - 1]['number'] /= tokens[index + 1]['number']
                del tokens[index:index + 2] 
            else:
                index += 1
        else:
            index += 1
    return tokens
 ```
 MULTIやDIVIDEの演算子を中心に条件分岐を行う<br>
 もし、現在のトークンが、MULTIかDIVIDEだった場合、<br>
 演算子トークンの1つ前の数字に、演算子トークンの1つ後の<br>
 数字を演算する
 
 
 #### 括弧内の式を評価する
 ```
 # calculate brackets
def evaluate_brackets(tokens):
    bracket_tokens = [] # 結果を格納する空配列
    index = 0
    count_brackts= 0 # 括弧の数を数える

    while index < len(tokens):
        if tokens[index]['type'] == 'LEFT_BRACKET':
            for i in range(index, len(tokens)):
                if tokens[i]['type'] == 'LEFT_BRACKET':
                    count_brackts += 1
                elif tokens[i]['type'] == 'RIGHT_BRACKET':
                    count_brackts -= 1
                    if count_brackts == 0:
                        result = evaluate(tokens[index + 1:i])
                        bracket_tokens.append({'type': 'NUMBER', 'number': result})
                        index = i
                        break
        else:
            bracket_tokens.append(tokens[index])
        index += 1
    if count_brackts != 0:
        print("Invalid syntax: Unbalanced brackets")
        exit(1)

    return bracket_tokens
 ```
 もし、開き括弧が出てきた場合、count_bracktsを1増やす<br>
 もし、閉じ括弧が出てきた場合、count_bracktsを1減らす<br><br>
 
 count_bracktが0の場合、evaluate関数を呼び出し、式を評価する<br>
 evaluate関数を呼び出した際に、evaluate_brackets関数が再帰的に呼び出されるため、<br>
 複数の括弧に対応している<br>
 
 ```
 result = evaluate(tokens[index + 1:i])<br>
 ```
 
 ex) (5+(8+9))<br>
 
 最初のcount_brackts == 0になったタイミング、つまり二重括弧の<br>
 1番右側までindexを進めた場合<br><br>
 
 evaluate関数には、index + 1:i、つまり5+(8+9)が引数として渡される<br>
 evaluate_brackets関数が再帰的に呼び出され、(8+9)が評価される<br>
 
 
 #### 関数を評価する
 ```
 
def evaluate_function(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] in ['ABS', 'INT', 'ROUND']:
            func_tokens = []
            func_type = tokens[index]['type']
            end_index = index + 1
            bracket_count = 0
            if end_index < len(tokens) and tokens[end_index]['type'] == 'LEFT_BRACKET': 
                bracket_count += 1
                end_index += 1
                while end_index < len(tokens):
                    if tokens[end_index]['type'] == 'LEFT_BRACKET':
                        bracket_count += 1
                    elif tokens[end_index]['type'] == 'RIGHT_BRACKET':
                        bracket_count -= 1
                        if bracket_count == 0:
                            break  
                    func_tokens.append(tokens[end_index])
                    end_index += 1
                if end_index < len(tokens) and tokens[end_index]['type'] == 'RIGHT_BRACKET':
                    func_result = evaluate(func_tokens)
                    if func_type == 'ABS':
                        result = abs(func_result)
                    elif func_type == 'INT':
                        result = int(func_result)
                    else: 
                        result = round(func_result)
                    tokens[index:end_index+1] = [{'type': 'NUMBER', 'number': result}]
                else:
                    print("Invalid syntax")  
                    exit(1)
            else:
                print("Invalid syntax")  
                exit(1)
        index += 1
    return tokens
 ```
 evaluate_brackets関数と同様に、括弧を数えていく
 ```
 func_result = evaluate(func_tokens)
 ```
 括弧の中に式があった場合、evaluate関数に渡し、式を評価する
 
 ```
 if func_type == 'ABS':
     result = abs(func_result)
 elif func_type == 'INT':
     result = int(func_result)
 else: 
     result = round(func_result)
 ```
 
 関数のタイプに応じて中の数値トークンを評価する
 ```
 tokens[index:end_index+1] = [{'type': 'NUMBER', 'number': result}]
 ```
 評価し終わった数値トークンに、tokensを置き換える
