f = open("piglatin2.in", "r")
text = f.readline().split(" ")
text[-1] = text[-1][:-1]
f.close()

def unPigLatin(word):
    if word[-3].lower() == "y":
        return word[:-3]
    if ord(word[0]) < 97:
        return word[-3].upper() + word[:-3].lower()
    return word[-3] + word[:-3]

unLatinText = [unPigLatin(elem) for elem in text]

f = open("piglatin2.out", "w")
f.write(" ".join(unLatinText) + "\n")
f.close()
