import sys

text = sys.argv[1]

def railcipher(toShift, numRails):
    outerDiff = 2*numRails - 2
    numIter = len(toShift) // outerDiff
    finalPos = len(toShift) % outerDiff

    shifted = [len(toShift)]
    k = 0
    for rail in range(0, numRails):
        for letter in range(0,
