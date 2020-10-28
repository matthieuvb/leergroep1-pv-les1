# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam:
# Problemomschrijving: Feest met functies!


#
# voorbeeldfunctie leng uit het college
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])

def flipside(s):
    """flipside swaps s's sides
       Argument s: a string
    """
    x = len(s) // 2
    return s[x:] + s[:x]


#
# Tests
#
assert flipside("zijkant") == "kantzij"
assert flipside("huiswerk") == "werkhuis"
assert flipside("flipside") == "sideflip"
assert flipside("az") == "za"
assert flipside("a") == "a"
assert flipside("") == ""

def mult(n, m):
    """mult returns the product of its two arguments
       Arguments: n and m are both integers
       Return value: the result of multiplying n and m
    """
    # jouw code komt hier (de body)
    #if m == 0:
        #return 1
    #else:
        #return (n + mult(n, m-1))
    if n == 0 or m == 0:
        return 0
    else:
        if n < 0 and m > 0:
            return n + mult(n, m - 1)
        elif n < 0 and m < 0:
            return -m + mult(-n - 1, -m)
        else:
            return m + mult(n - 1, m)

assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0

def dot(L, k):
    if L == "" or k == "":
        return 0.0
    elif len(L) != len (k):
        return 0.0
    else:
        return sum([L[i] * k[i] for i in range(len(L))]) 

assert dot([5, 3], [6, 4]) == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0

def ind(e,L):
    if e in L:
        for index, item in enumerate(L):
            if item == e:
                return index
        return index+1

    if e not in L:
        return len(L)
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5

def letter_score(let):
    if let in "adeinorst":
        return 1
    elif let in "ghl":
        return 2
    elif let in "bcmp":
        return 3
    elif let in "jkuvw":
        return 4
    elif let in "f":
        return 5
    elif let in "z":
        return 6
    elif let in "xy":
        return 8
    elif let in "q":
        return 10
    else:
        return 0

def scrabble_score(s):
    if s == '':
        return 0
    elif s[0] in "adeinorst":
        return 1 + scrabble_score(s[1:])
    elif s[0] in "ghl":
        return 2 + scrabble_score(s[1:])
    elif s[0] in "bcmp":
        return 3 + scrabble_score(s[1:])
    elif s[0] in "jkuvw":
        return 4 + scrabble_score(s[1:])
    elif s[0] in "f":
        return 5 + scrabble_score(s[1:])
    elif s[0] in "z":
        return 6 + scrabble_score(s[1:])
    elif s[0] in "xy":
        return 8 + scrabble_score(s[1:])
    elif s[0] in "q":
        return 10 + scrabble_score(s[1:])
    else:
        return 0 + scrabble_score(s[1:])

assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0

def one_dna_to_rna(c):
    """Converts a single-character c from DNA nucleotide
       to complementary RNA nucleotide
    """
    if c == 'A':
        return 'U'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    else:
        return ''

def transcribe(s):
    if len(s)==0:
        return ''
    else:
        return one_dna_to_rna(s[0]) + transcribe(s[1:])
