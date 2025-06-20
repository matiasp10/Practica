# =============================================
# Ejercicio: MakeUpperCase
# Plataforma: Codewars
# Enlace: https://www.codewars.com/kata/54b81566cd7f51408300022d/train/python
# Autor: Matias Petenatti
# Fecha: 2025-06-20
# Descripción:

# Write a method that will search an array of strings for all strings that contain another string, ignoring capitalization. Then return an array of the found strings.

# The method takes two parameters, the query string and the array of strings to search, and returns an array.

# If the string isn't contained in any of the strings in the array, the method returns an array containing a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)
# Examples

# If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], the method should return ["home", "Mercury"].

# =============================================

def word_search(query, seq):
    result = []
    for word in seq:
        if query.lower() in word.lower():
            result.append(word)
    if len(result) == 0:
        result.append("None")
        return result
    else:
        return result

word_search("ab", ["za", "ab", "abc", "zab", "zbc"])
word_search("aB", ["za", "ab", "abc", "zab", "zbc"])
word_search("ab", ["za", "aB", "Abc", "zAB", "zbc"])
