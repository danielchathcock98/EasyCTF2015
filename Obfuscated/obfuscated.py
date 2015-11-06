from string import ascii_uppercase as v, ascii_lowercase as k

def check_flag(s):
        if len(s) != 0x19:
                print "len"
                return False
	s = list(s)
	if int(`[s.pop(r) for r in ([2] + [i for i in range(11, 18, 2)] + [20])[::-1]][::-1]`[2::5]) != 0x61a83:
                print "2, 11, 13, 15, 17, 20"
                return False
        print s
	if len(list(set([s.pop(r) for r in map(lambda p: int(p, 2), [("1"*5)[:2], ("1"*5)[2:]])[::-1]]))) != s.index("h"):
                print "3,7 and 1"
                return False
        print s
	y, z = [], []
	u = len(list(set([repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]))) - 1
	if u != len(list(set(y))) ^ len(list(set(z))):
                print "same 24 22 and 23 21"
                return False
	if (ord(y[u]) ^ ord(z[u])) ^ 0x1e != 0:
                print "24 xor 23"
                return False
	if v.index(s.pop()) ^ len(s) ^ 0x1e != 0:
                print "19 xor 12?"
                return False
	a, i = filter(lambda c: c in v, s), filter(lambda c: c in k, s)
	if map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 != map(ord, a):
                print "uppers are WRTHOOOO"
                return False
	i[1:3] = i[2:0:-1]
	if i != list("hate"):
                print "hate"
                return False
	return True


print "hi?"
check_flag(raw_input("Go\n"))
