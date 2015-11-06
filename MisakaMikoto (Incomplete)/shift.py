import sys

ciphertext = sys.argv[1]
key = sys.argv[2]

# shift any lowercase or capital letter by n
def shiftN(char, n):
    charOrd = ord(char)
    if charOrd > 64 and charOrd < 91:
        return chr((charOrd-65+n)%26+65)
    elif charOrd > 96 and charOrd < 123:
        return chr((charOrd-97+n)%26+97)
    return char

def shiftAllN(char, n):
    return chr(ord(char) + n)

# shift the entire string
def doCaeser(text, shiftNum):
    return "".join([shiftAllN(letter, shiftNum) for letter in list(text)])

print(doCaeser(ciphertext, 0) + "\n\n")

i = -97
newText = "".join([chr(ord(char) + ord(key[i % len(key)])) for i, char in enumerate(ciphertext)])
nextin = input(doCaeser(newText, i))
while nextin != "":
    if nextin == "x":
        i += 1
    else: i -= 1
    nextin = input(doCaeser(newText, i))
