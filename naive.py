import time
import string
import random

def create_dictionary():
    words = '/usr/share/dict/words'
    dictionary = set()
    with open(words,'r') as wf:
        words = wf.readlines()
        for word in words:
            if len(word) > 5:
                dictionary.add(word.upper().strip())

    return dictionary

def check_wordlist(wordlist, key, check):
    count = 0
    for word in wordlist:
        cur = set(word)
        if key in word and cur.issubset(check):
           # print(word)
            count += 1
    #print("------------------------")
    return count

def solve (wordlist, puzzles):
    result = []
    for word in puzzles:
        cur = set(word)
        result.append(check_wordlist(wordlist, word[0], cur))
    return result

def get_letters():
    alphabet_list = list(string.ascii_uppercase)
    vowels = ['A','E','I','O','U']
    while True:
	# generate sample of alphabet (can inlcude each letter only once)
        random_list = random.sample(alphabet_list, 7)

	# make sure each letter list includes at least one vowel
        if [i for i in random_list if i in vowels]:
            return ''.join(random_list)
#puzzles = []
#for i in range(25):
#    puzzles.append(get_letters())

wordlist = create_dictionary()
puzzles = ['VSKFLIP', 'HLOUYFP', 'ARJSOZX', 'WGHUELV', 'ZUKBHXS', 'POKNIMF', 'EZOPKBW', 'WXUYZLH', 'PLZWUQB', 'BOVMYAW', 'POJIVAU', 'YECZRTA', 'LCGFOHD', 'NACWEHO', 'VWEPZBN', 'VIGNJDZ', 'KOMHWRF', 'OARHBFE', 'YIGZUNM', 'SJYOAEG', 'GPJUMIW', 'MUVSEYZ', 'CSXJOGE', 'SATMCVW', 'WGXCSIB']

then = time.time()

print(solve(wordlist, puzzles))

now = time.time()

print("It took: ", now-then, " seconds")
