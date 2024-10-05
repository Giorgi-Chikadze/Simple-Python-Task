def check_dupes(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            if text[i] == text[j]:
                return False
        return True
        


a = check_dupes("asdfgh")
print(a)
