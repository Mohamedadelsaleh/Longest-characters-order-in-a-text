while True:
    text = input("Enter Your Text: ").strip()
    if text.isalpha():
        text = str(text)
        break


def subStringOrder(userText):
    longest = userText[0]
    current = userText[0]
    for i in userText[1:]:
        if i >= current[-1]:
            current += i
            if len(current) > len(longest):
                longest = current
        else:
            current = i
    return longest


restStr = subStringOrder(text)
print("Longest subString in your text is : ", restStr)
