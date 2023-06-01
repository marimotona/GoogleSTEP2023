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
    return token, index + 3

def read_int(line, index):
    token = {'type': 'INT'}
    return token, index + 3

def read_round(line, index):
    token = {'type': 'ROUND'}
    return token, index + 5


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
        elif line[index:index+3] == 'abs':
            (token, index) = read_abs(line, index)
        elif line[index:index+3] == 'int':
            (token, index) = read_int(line, index)
        elif line[index:index+5] == 'round':
            (token, index) = read_round(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

# print(tokenize("3+6"))


def parse_rpn(line):
    stack = []
    operator = []

    for char in line:
        if char.isdigit():
            stack.append(char)
        else:
            operator.append(char)
    stack.extend(operator)
    return ''.join(stack)

# def parse_rpn(tokens):
#     numbers = []
#     operators = []
#     index = 0

#     while index < len(tokens):
#         if tokens[index]['type'] == 'NUMBER':
#             numbers.append(tokens[index])
#         else:
#             operators.append(tokens[index])
#         index += 1
        
#     numbers.append(operators)
#     return numbers

# def parse_rpn(tokens):
#     numbers = []
#     operators = []

#     for token in tokens:
#         if token['type'] == 'NUMBER':
#             numbers.append(token)
#         else:  # it's an operator
#             operators.append(token)

#     numbers.append(operators)
#     return numbers


print(tokenize(parse_rpn("3+4")))


# calculate plus and minus
def evaluate_plus_minus(tokens):
    stack = []
    for token in tokens:
        if token['type'] == 'NUMBER':
            stack.append(token['number'])
        elif token['type'] in ['PLUS', 'MINUS']:
            if len(stack) < 2:
                print('Invalid syntax')
                exit(1)
            number2 = stack.pop()
            number1 = stack.pop()
            if token['type'] == 'PLUS':
                stack.append(number1 + number2)
            elif token['type'] == 'MINUS':
                stack.append(number1 - number2)
        else:
            print('Invalid syntax')
            exit(1)
    if len(stack) != 1:
        print('Invalid syntax')
        exit(1)
    return stack.pop()





def evaluate(tokens):
    return evaluate_plus_minus(tokens)



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
    test("3+5")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)