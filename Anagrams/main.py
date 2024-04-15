# https://train.nzoi.org.nz/problems/471

# @def str, str -> None
def anagram(prefix, sub):
    if len(sub) == 1:
        permutation = prefix + sub
        if permutation != word:
            print(permutation)
        return
    for i, letter in enumerate(sub):
        s = sub[:i] + sub[i + 1:]
        anagram(prefix + letter, s)

word = input()
anagram("", word)