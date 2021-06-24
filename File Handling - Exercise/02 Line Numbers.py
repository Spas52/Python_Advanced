import os, re


def get_words_list(path_to_file):
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as file:
            text = file.readlines()
            return text


def get_lines(text):
    words = []
    for i in range(len(text)):
        letters_count = 0
        punctuation_marks = 0
        text[i] = re.sub(r'[\n]', '', text[i])
        punctuation_marks = len(re.findall(r'[-,.!?\']', text[i]))
        letters_count = len(re.findall(r'[a-z]', text[i].lower()))
        words.append(f'Line {i+1}: {text[i]} ({letters_count})({punctuation_marks})')
    return words


def print_result(words):
    with open("line_numbers_output.txt", 'w') as file:
        for i in range(len(words)):
            file.write(words[i])
            file.write('\n')


path_to_text = 'line_numbers.txt'
text = get_words_list(path_to_text)
words = get_lines(text)
print_result(words)