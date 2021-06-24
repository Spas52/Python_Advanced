import os, re


def get_words_list(path_to_file):
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as file:
            text = ''.join(file.readlines())
            return re.findall(r"[a-z']+", text.lower())


def get_result(words_to_count, input_words):
    word_count = {}
    for word in words_to_count:
        if word in input_words:
            word_count[word] = input_words.count(word)
    return word_count


def print_result(word_count):
    word_count = dict(sorted(word_count.items(), key=lambda s: -s[1]))
    for word, count in word_count.items():
        print(f'{word} - {count}')


path_to_words = "words.txt"
path_to_input = "input.txt"
words_to_count = get_words_list(path_to_words)
input_words = get_words_list(path_to_input)
word_count = get_result(words_to_count, input_words)
print_result(word_count)