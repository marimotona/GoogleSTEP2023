while True:
    line = input()
    answer = 0.0
    index = 0
    ope = 1
    while index < len(line):
        number = 0.0
        while index < len(line) and (line[index].isdigit() or line[index] == '.'):
            if line[index] == '.':
                index += 1
                decimal_place = 1
                while index < len(line) and line[index].isdigit():
                    number = number + int(line[index]) / (10 ** decimal_place)
                    print("number = %f\n" % number)
                    print("answer = %f\n" % answer)
                    decimal_place += 1
                    index += 1
                break
            else:
                number = number * 10 + int(line[index])
                print("number = %f\n" % number)
                index += 1
        if ope == 1:
            answer += number 
        elif ope == 2: #最初の数字がここに入ってしまうから
            answer -= number  

        if index < len(line):         
            if line[index] == '+':
                index += 1
                ope = 1
            elif line[index] == '-':
                index += 1
                ope = 2
            else:
                print('Invalid character found: ' + line[index])
                exit(1)
    print("answer = %f\n" % answer)

# 直前の演算子をみるようにする、indexの一個前をみる
# モジュール化、関数の責任範囲を明確にする
# モジュール化、チームネコ
# readNumberの関数をいじるのみ、あっちこっち変更しなくてもよい
# 何をする関数なのか
# 関数をしっかりモジュール化できると、コードを全部読まなくてもいいのか
# そうすると関数の組み合わせ、呼び出しのみで機能を実装することが出来る