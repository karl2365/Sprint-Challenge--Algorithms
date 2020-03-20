'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # initialize an incrementer
    result = 0
    # base case
    if len(word) == 0:
        return 0
    # Find out increment condition
    if word[:2] == "th":
        result = 1
    # sum incrementing results
    return result + count_th(word[1:])


word = "abcthefthghith"
print(count_th(word))

