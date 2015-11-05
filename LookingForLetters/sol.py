f = open("looking-for-letters.in", "r")
text = f.readline()
f.close()
f = open("looking-for-letters.out", "w")

f.write(",".join([num for num in text if num.isdigit()]) + "\n")

f.close()
