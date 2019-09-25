import time
import string
import random

class Trie():
    head = {}

    def add(self,word):
        cur = self.head
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = True

def find_words(puzzle, key, letter, neighbors, check):
    count = 0
    if '*' in neighbors and key in check:
      #print(check)
      count += 1
    for k, _ in neighbors.items():
        if k in puzzle or '*' in puzzle:
            count += find_words(puzzle, key, k, neighbors[k], check + k)
    return count

def scan_puzzle(wordlist, puzzle, key, letter):
    if letter not in wordlist:
        return 0
    return find_words(puzzle, key, letter, wordlist[letter], letter)

def solve(wordlist, puzzles):
    result = []
    for chars in puzzles:
        key = chars[0]
        count = 0
        for ch in chars:
            count += scan_puzzle(wordlist, chars, key, ch)
        result.append(count)

    return result

def create_dictionary():
    words = '/usr/share/dict/words'
    dictionary = set()
    with open(words,'r') as wf:
        words = wf.readlines()
        for word in words:
            if len(word) > 5:
                dictionary.add(word.upper().strip())

    return dictionary
then = time.time()
trie = Trie()
wordlist = create_dictionary()
for word in wordlist:
    trie.add(word)
puzzles = ['VSKFLIP', 'HLOUYFP', 'ARJSOZX', 'WGHUELV', 'ZUKBHXS', 'POKNIMF', 'EZOPKBW', 'WXUYZLH', 'PLZWUQB', 'BOVMYAW', 'POJIVAU', 'YECZRTA', 'LCGFOHD', 'NACWEHO', 'VWEPZBN', 'VIGNJDZ', 'KOMHWRF', 'OARHBFE', 'YIGZUNM', 'SJYOAEG', 'GPJUMIW', 'MUVSEYZ', 'CSXJOGE', 'SATMCVW', 'WGXCSIB']


print(puzzles)
print(solve(trie.head, puzzles))

now = time.time()

print("It took: ", now-then, " seconds")

