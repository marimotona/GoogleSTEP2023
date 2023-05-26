while True:
    line = input()
    answer = 0
    index = 0
    while index < len(line):
       ope = 1
       flag_point = 0
       flag_float = 0
       number = 0
       if line[index].isdigit() or line[index] == '.':
           if line[index] == '.':
              flag_point == 1
           while index < len(line) and line[index].isdigit():
               number = number * 10 + int(line[index])
               index += 1
               if ope == 1:
                answer += number 
               elif ope == 2: #最初の数字がここに入ってしまうから
                answer -= number           
       elif line[index] == '+':
           index += 1
           ope += 1
       elif line[index] == '-':
           index += 1
           ope += 1
       else:
           print('Invalid character found: ' + line[index])
           exit(1)
    print("answer = %d\n" % answer)

# 直前の演算子をみるようにする、indexの一個前をみる
# モジュール化、関数の責任範囲を明確にする
# モジュール化、チームネコ
# readNumberの関数をいじるのみ、あっちこっち変更しなくてもよい
# 何をする関数なのか
# 関数をしっかりモジュール化できると、コードを全部読まなくてもいいのか
# そうすると関数の組み合わせ、呼び出しのみで機能を実装することが出来る