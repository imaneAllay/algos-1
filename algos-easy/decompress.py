# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.
import gzip
def decompress(s):
    result = []
    i = 0

    while i < len(s):
        if not s[i].isdigit():
            result.append(s[i])
            i += 1
        else:
            count = int(s[i])
            letter = s[i + 1]
            result.append(letter * count)
            i += 2

    return ''.join(result)



# TEST CASE
print(decompress("2c3a1t"))
# print(decompress("4s2b") )# -> 'ssssbb'
# print(decompress("2p1o5p")) # -> 'ppoppppp'
# print(decompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
# print(decompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
