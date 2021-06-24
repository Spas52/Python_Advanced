import os, re


def get_words_list(path_to_file):
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as file:
            text = file.readlines()
            return text


def get_even_lines(text):
    words = []
    for i in range(len(text)):
        if i % 2 == 0:
            text[i] = re.sub(r'[-,.!?]', '@', text[i])
            text[i] = re.sub(r'[\n]', '', text[i])
            words.append(text[i].split())
    return words


def print_result(words):
    for i in range(len(words)):
        words[i] = words[i][::-1]
        print(' '.join(words[i]))


path_to_text = "even_lines.txt"
text = get_words_list(path_to_text)
words = get_even_lines(text)
print_result(words)