import sys, itertools

f1 = open(sys.argv[1], "r")
text1 = "".join([val for line in f1.read().strip().split("\n") for val in line.split(" ")])
f1.close()

f2 = open(sys.argv[2], "r")
text2 = "".join([val for line in f2.read().strip().split("\n") for val in line.split(" ")])
f2.close()
assert len(text1) == len(text2)

text = ""
for letter in range(0, len(text1), 16):
    char = ""
    for comp in range(letter, letter + 16, 2):
        if text1[comp:comp+2] == text2[comp:comp+2]:
            char += "0"
        else:
            char += "1"
    text += chr(int(char, 2))

print(text)
