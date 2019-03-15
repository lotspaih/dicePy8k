#!/usr/bin/env python3

# Copyright 2017 Mark Lotspaih
# MIT License https://opensource.org/licenses/MIT

# dicePy8k - Pseudorandom word generator for Diceware 8k passwords
# USE: Run this file from the command line adding a number for the
#    word length as an argument or input length as needed.
# VERSION: 02/01/2018


import os
import sys
import random
from pathlib import Path
import webbrowser


def genRandomWords(words):
    '''Pseudorandomly pick a requested number of words
    from the diceware8k.txt file, add it to a list,
    and return the list.'''
    wordList = []
    for i in range(0, int(words)):
        seed = os.urandom(32)
        rint = random.SystemRandom(seed)
        wordList.append(
         diceStringList[rint.randint(0, len(diceStringList))].strip('\n'))
    return wordList


# Assign path for diceware list file
scriptPath = os.path.dirname(os.path.realpath(sys.argv[0]))
diceListPath = Path(scriptPath + '/diceware8k.txt')

# Verify the diceware8k.txt text file exists in the current working directory
# If it does not exist, then open default web browser to download link
if not os.path.isfile(diceListPath):
    print('The diceware8k.txt file was not found in the current working'
          ' directory!')
    try:
        webbrowser.open(
            'http://world.std.com/~reinhold/dicewarefaq.html#electronic')
    except:
        print('There was a problem opening the link to download the'
              ' diceware8k.txt file.')
    sys.exit(1)

# Open the diceware8k.txt and save lines as list to variable
with open(diceListPath) as dicewordList:
    diceStringList = dicewordList.readlines()

# Request user input on the amount of words from CLI or input
if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        words = sys.argv[1]
    else:
        print('The CLI argument must be a number or blank!')
        sys.exit(1)
elif len(sys.argv) < 2:
    while True:
        words = input('How many words do you want for your Diceware '
                      'passphrase?: ')
        if words.isdigit():
            break
        print('ERROR: You must enter a number!\n')

# Run pseudorandom function and get return list
wordListReturned = genRandomWords(words)
print('')
print('Here are your {} pseudorandom words from the 8k Diceware List:'
      .format(words))
print('')

# Print word list and pause for user to copy or record word list
wordListString = ''
for word in wordListReturned:
    wordListString = wordListString + word + ' '
print(wordListString)
print('')
if os.name == 'nt':
    os.system('pause')
else:
    input('Press Return/Enter to continue...')

sys.exit(0)
