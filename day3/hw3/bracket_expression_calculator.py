#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def read_multi(line, index):
    token = {'type': 'MULTI'}
    return token, index + 1

def read_left_bracket(line, index):
    token = {'type': 'LEFT_BRACKET'}
    return token, index + 1

def read_right_bracket(line, index):
    token = {'type': 'RIGHT_BRACKET'}
    return token, index + 1


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
        elif line[index] == '(':
            (token, index) = read_left_bracket(line, index)
        elif line[index] == ')':
            (token, index) = read_right_bracket(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate_expression_brackets(tokens, index):
    index += 1

    bracket_tokens = []
    while index < len(tokens) and tokens[index]['type'] != 'RIGHT_BRACKET':
        bracket_tokens.append(tokens[index])
        index += 1

    result = evaluate(bracket_tokens)

    return {'type': 'NUMBER', 'number': result}, index + 1


def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    priority_tokens = []

    while index < len(tokens):
        if tokens[index]['type'] == 'LEFT_BRACKET':
            (token, index) = evaluate_expression_brackets(tokens, index)
            if len(priority_tokens) > 0 and priority_tokens[-1]['type'] in ['MULTI', 'DIVIDE']:
                operation = priority_tokens.pop() 
                if operation['type'] == 'MULTI':
                    priority_tokens[-1]['number'] *= token['number'] 
                else:
                    priority_tokens[-1]['number'] /= token['number']
            else:
                priority_tokens.append(token)
            print(priority_tokens)
        if index < len(tokens) and tokens[index]['type'] == 'NUMBER':
            if len(priority_tokens) > 0 and priority_tokens[-1]['type'] in ['MULTI', 'DIVIDE']:
                operation = priority_tokens.pop() # 'multi'や'divideの演算子を取り出している
                if operation['type'] == 'MULTI':
                    priority_tokens[-1]['number'] *= tokens[index]['number'] # priority_tokensの最後の要素と、今の要素を計算する
                else:
                    priority_tokens[-1]['number'] /= tokens[index]['number']
            else:
                priority_tokens.append(tokens[index])
        elif index < len(tokens):
            priority_tokens.append(tokens[index])
        index += 1  

    print(priority_tokens)

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



def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("(3+4)-5")
    test("1*(3+5)-6")
    test("(3+4*(2-1))/5")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
