'''

与えられた文字列のanagramを辞書ファイルから探して、
「見つかったアナグラム全部」を答えるプログラムを作る

'''

# 二分探索で書き直す
# 最初に並び替えして、二分探索を行う、検索が複数回行われる場合、最初にソートした辞書を使う


def search_anagram(ramdom_word, filename):
    sorted_word = ''.join(sorted(ramdom_word))

    with open(filename, 'r') as f:
        dictionary = f.read().splitlines()

    new_dictionary = [(''.join(sorted(word)), word) for word in dictionary]

    anagram = []
    for i in new_dictionary:
        if i[0] == sorted_word:
            anagram.append(i[1])
    return anagram


print(search_anagram('cat', 'data/anagram/words.txt'))
print(search_anagram('', 'data/anagram/words.txt') == [])
print(search_anagram('a', 'data/anagram/words.txt'))
print(search_anagram('statueofliberty', 'data/anagram/words.txt'))
print(search_anagram('silent', 'data/anagram/words.txt'))