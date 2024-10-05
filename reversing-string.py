def reversed_string(text):
    reversed = ""
    for i in text:
       reversed = i + reversed

    return reversed

c = reversed_string("bankai")
print(c)


