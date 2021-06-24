def is_vowel(character):
    if character.lower() in "aeouei":
        return True
    return False


print("".join([char for char in input() if not is_vowel(char)]))
