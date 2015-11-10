username = "evil@anomat.cf"

userbytes = list(map(ord, username))

print(userbytes)

def firstloop():
    val = 0x1337
    for byte in userbytes:
        val = val ^ byte
    return val

var_30 = firstloop()
print(hex(var_30))

def secondloop():
    cal = 0xdeadfa11
    for i in range(0, 25, 5):
