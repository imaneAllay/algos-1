# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  # def anagrams(s1, s2):
  #   if len(s1) == len(s2):
  #     for c1 in s1:
  #       if c1 not in s2:
  #         return False
  #     for c2 in s2:
  #       if c2 not in s1:
  #         return False
  #
  # return True

  return sorted(s1) == sorted(s2)








  #if len s1 eq len s2
  # and all caracter in s1  exist in s2
  # for c in s1:
  #   if c not in s2:
  #     return False
  #   for ca in s2:
  #     if ca not in s1:
  #       return False
  #
  # return True



# # TEST CASES
print(anagrams('restful', 'fluster')) # -> True
print(anagrams('cats', 'tocs') )# -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi') )# -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
