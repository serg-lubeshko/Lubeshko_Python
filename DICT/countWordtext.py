""""Программа выводит в алфавитном порядке (с учетом регистра) список слов и количеством вхождений каждого из них

"""

import string

words = {}
string_ = string.whitespace + string.punctuation + string.digits + "\"'"
for line in open("text.txt", encoding="utf-8"):
    for word in line.split():
        word = word.strip(string_)
        if len(word) > 2:
            words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print(f'{word} - meets {words[word]} times')
