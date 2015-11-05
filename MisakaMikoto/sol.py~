cyphertext = "Cnebnl Vtxltk bl max uxlm unm fr ykbxgw ebdxl Gtihexhg uxmmxk yhk patmxoxk kxtlhg. Ha pxee. Max yetz bl xtlrvmy{Gti0exhg_ol_Vt3l4k}"

# shift any lowercase or capital letter by n
def shiftN(char, n):
    charOrd = ord(char)
    if charOrd > 64 and charOrd < 91:
        return chr((charOrd-65+n)%26+65)
    elif charOrd > 96 and charOrd < 123:
        return chr((charOrd-97+n)%26+97)
    return char

# shift the entire string
def doCaeser(text, shiftNum):
    return "".join([shiftN(letter, shiftNum) for letter in list(text)])

print(doCaeser(cyphertext, 0) + "\n\n")

i = 0
while input(doCaeser(cyphertext, i)) == "":
    i += 1
