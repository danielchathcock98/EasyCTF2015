f = open("piglatin1.in", "r")
text = f.readline().split(" ")
text[-1] = text[-1][:-1]
f.close()

def makePigLatin(word):
    if word[0].lower() in ['a','e','i','o','u']:
        return word + "yay"
    return word[1:] + word[0] + "ay"

latinText = [makePigLatin(elem) for elem in text]

f = open("piglatin1.out", "w")
f.write(" ".join(latinText) + "\n")
f.close()
