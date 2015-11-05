f = open("string-change.in", "r")
nums = [int(num) for num in f.readline().split(",")]
text = list(f.readline())[:-1]
f.close()

changedText = [letter for letter in text]

for num in nums:
    for i in range(num, len(text), num):
        if changedText[i] == text[i]:
            changedText[i] = chr(ord(text[i]) + 1)
            if ord(changedText[i]) == 91 or ord(changedText[i]) == 123:
                changedText[i] = chr(ord(changedText[i]) - 26)

f = open("string-change.out", "w")
f.write("".join(changedText) + "\n")
f.close()
