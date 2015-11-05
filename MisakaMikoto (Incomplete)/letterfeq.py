import sys, collections
f = open(sys.argv[1], "r")

text = f.read()
f.close()

letters = collections.Counter(text)

print(letters)
