'''

与えられた文字列の全てを使わなくてもよいように
関数をアップグレードする

'''
# import collections

from collections import Counter

'''

sortする.ver

def maxscore_anagram(word_data, filename):
    with open(word_data, 'r') as w:
        lines = w.read().splitlines()

    with open(filename, 'r') as f:
        dictionary = f.read().splitlines()

    new_worddata, char_data = [], []
    for l in lines:
        new_worddata.append(''.join(sorted(l)))
        char_data.append(collections.Counter(l))

    new_dictionary = [(''.join(sorted(word)), word, collections.Counter(word)) for word in dictionary]

    print(new_dictionary)
    anagram = []
    
    return anagram

'''

def maxscore_anagram(word_data, filename):
    with open(word_data, 'r') as w:
        lines = w.read().splitlines()

    with open(filename, 'r') as f:
        dictionary = f.read().splitlines()
    
    new_worddata = [(line, Counter(line)) for line in lines]

    new_dictionary = [(word, Counter(word)) for word in dictionary]

    anagram = [ele[0] for ele in new_dictionary if ele[1] == new_worddata[1]]
    
    return anagram

# maxscore_anagram('data/anagram/large.txt', 'data/anagram/words.txt')


def test(word, testfile):
    with open(testfile, 'r') as f:
        test_dictionary = f.read().splitlines()
    
    count_word = Counter(word)

    test_new_dictionary = [(word, Counter(word)) for word in test_dictionary]

    anagram = [ele for ele in test_dictionary if not Counter(ele) - count_word]
    
    return anagram

# print(test('data/anagram/small.txt', 'data/anagram/words.txt'))


###############################

# Counterメソッドを自分で実装してみる
# Counterの中身を見てみるとか、自分で新たに用意するとか
# 内部のベクトルを、自分で配列を用意する



SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]

def calculate_score(word):
    score = 0
    for character in list(word):
        score += SCORES[ord(character) - ord('a')]
    return score


def make_highscore_sorted_dictionary(dictionary):
    dictionary_with_score = []
    for word in dictionary:
        score = calculate_score(word)
        dictionary_with_score.append((word, score, Counter(word)))
    dictionary_with_score.sort(key=lambda x: x[1], reverse=True)
    return dictionary_with_score


def find_best_anagram(word, dictionary):

    count_word = Counter(word)

    for ele in dictionary:
        if(len(Counter(ele[0]) - count_word) == 0):
            return ele[0]
        
    return ''

'''
def highest_score(output_anagrams):
    max_score = 0
    best_anagram = ''
    for c in output_anagrams:
        score = calculate_score(c)
        if score > max_score:
            max_score = score
            best_anagram = c

    return best_anagram
'''


if __name__ == "__main__":
    with open('data/anagram/words.txt', 'r') as f:
        dictionary = f.read().splitlines()
    
    new_dictionary = make_highscore_sorted_dictionary(dictionary)

    directory_name = 'data/anagram/'
    fileName = ['small', 'medium', 'large']

    for j in range(len(fileName)):
        with open(directory_name + fileName[j] + '.txt', 'r') as f:
            input_file_word = f.read().splitlines()

        answer_list = []
        for ele in input_file_word:
            output_anagram = find_best_anagram(ele, new_dictionary)

            if len(output_anagram) == 0:
                answer_list.append('')
            else:
                answer_list.append(output_anagram)

        with open(directory_name + fileName[j]+ '_answer' + '.txt', 'w') as f:
            for ele in answer_list:
                f.write(ele+'\n')