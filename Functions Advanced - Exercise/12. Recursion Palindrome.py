def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    elif not word[index] == word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)



