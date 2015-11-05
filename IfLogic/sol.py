f = open("if-logic.in", "r")
nums = f.readline().split(",")
nums[-1] = nums[-1][:-1]
nums = [int(elem) for elem in nums]

f.close()
f = open("if-logic.out", "w")

string = ""

for num in nums:
    if num >= 0 and num <= 50:
        string = "hi\n"
    elif num >= 51 and num <= 100:
        string = "hey\n"
    else:
        string = "hello\n"
    f.write(string)
    f.flush()

f.close()
