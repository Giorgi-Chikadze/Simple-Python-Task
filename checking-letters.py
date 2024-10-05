def check_letters(text):
    letter_dict = {}
    for i in text:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    return letter_dict




b = check_letters("illuminate")
print(b)
