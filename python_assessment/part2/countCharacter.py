def count_characters(text):
    vowels=0
    consonants=0
    digits=0
    spaces=0

    for ch in text:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1

    return vowels,consonants,digits,spaces

v,c,d,s=count_characters("Python 123")

print("Vowels: ",v)
print("consonants: ",c)
print("digits: ",d)
print("spaces: ",s)
