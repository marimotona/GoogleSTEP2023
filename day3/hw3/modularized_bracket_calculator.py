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

def read_abs(line, index):
    token = {'type': 'ABS'}
    return token, index + 1

def read_int(line, index):
    token = {'type': 'INT'}
    return token, index + 1

def read_round(line, index):
    token = {'type': 'ROUND'}
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
        elif line[index] == 'abs':
            (token, index) = read_abs(line, index)
        elif line[index] == 'int':
            (token, index) = read_int(line, index)
        elif line[index] == 'round':
            (token, index) = read_round(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

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


def evaluate_brackets(tokens):
    bracket_tokens = []
    index = 0

    while index < len(tokens):
        if tokens[index]['type'] == 'LEFT_BRACKET':
            count_brackts = 0
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
    return bracket_tokens



def evaluate(tokens):
    # tokens = evaluate_function(tokens)
    tokens = evaluate_brackets(tokens)
    tokens = evaluate_mul_div(tokens)
    return evaluate_plus_minus(tokens)



def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))

tokens = [1, 2, 3, 4, 5]

print(tokens[2:4])

del tokens[2:4]

print(tokens)

# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("3+5")
    test("3*5+6")
    test("(3+4)-5")
    test("((3+4)-5)+8")
    # test("1*(3+5)-6")
    # test("(3+4*(2-1))/5")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
