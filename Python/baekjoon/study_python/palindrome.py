from audioop import reverse


def palindrome():
    word = input()
    new_word = word[::-1]

    if word == new_word:
        print(1)

    else:
        print(0)
palindrome()