import sys, collections

text = list(sys.argv[1])
textaspairs = []
for i in range(0, len(text), 2):
    textaspairs.append(text[i] + text[i + 1])

letters = collections.Counter(textaspairs)

print(letters)
