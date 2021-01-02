#!/usr/bin/env python

'''
index = 0
fruit = 'orange'
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

index = 0
fruit = 'orange'
for letter in fruit:
    print(letter)
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1

print(count)

word1 = 'apples'
word2 = 'oranges'
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
print(in_both(word1, word2))

word = 'banana'
if word == 'banana':
    print('All right, bananas!')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
'''

word1 = 'pots'
word2 = 'stop'
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
if word1 != word2:
    print True

i = 0
j = len(word2)

while j > 0:
    print(i, j)
    if word1[i] != word2[i]:
        i = i + 1
        j = j - 1


