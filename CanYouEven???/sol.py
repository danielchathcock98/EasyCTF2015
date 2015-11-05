f = open("can-you-even.in", "r")
nums = f.readline().split(",")
f.close()
f = open("can-you-even.out", "w")

# my little elem & 1 == 0 is just a bitwise check for and even number.
# yay for list comprehensions!!
f.write(str(len([elem for elem in nums if (int(elem)&1 == 0)])) + "\n")
f.flush()
f.close()
