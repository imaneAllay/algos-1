# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.
# def compres(s):


def compress(s):
    s += '.'  # Add a sentinel character to ensure the last character is processed
    result = []
    i, j = 0, 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            letter_count = j - i
            if letter_count == 1:
                result.append(s[i])
            else:
                result.append(str(letter_count))
                result.append(s[i])
            i = j

    return ''.join(result)


# TEST CASE
print(compress('ccaaatsss'))  # Output: '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')) # -> '127y'
