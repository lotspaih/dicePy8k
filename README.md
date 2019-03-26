[![GitHub license](https://img.shields.io/badge/license-MIT-green.svg)](https://gitlab.com/lotspaih/dicePy8k/blob/master/LICENSE) [![Language](https://img.shields.io/badge/language-python-blue.svg)](https://www.python.org/) 

# DicePy8k
DicePy8k is a very simple [Diceware](http://world.std.com/~reinhold/diceware.html) based passphrase generator written in Python using Diceware's 8k word list file for computer based pseudorandom generated Diceware passphrases.

## Purpose and Background
Wanting to try out my freshly acquired Python skills (thanks [Al](https://github.com/asweigart)), and needing to generate decent passphrases quickly without using real dice; I created the DicePy8k script for fun and function.

This script quickly generates multiple passphrase chunks (or words) that are somewhat easier to remember using mnemonics. However, per Arnold G. Reinhold, the creator of the Diceware password lists, there are drawbacks to using a computer and a programming language's random library to generate the passphrases.

>Generating truly random numbers using a computer is very tricky. The so-called random number generators that come with most programming libraries are nowhere near good enough. For most users dice is by far a better way to select passphrase words.

>However if you do know what you are doing, have access to a strong method for generating random numbers...and really need to generate passphrases using a computer, then, to insure a uniform distribution of words, it is best to using a list of words that is a whole power of two in length.

So, for a much more secure passphrase it is **HIGHLY** recommended that you use the Diceware list with real world dice to generate the random words! If you just need a quick and simple way to generate a passphrase, then using the Diceware 8k list (*"a whole power of two in length"*) to pseudorandomly generate a passphrase may be acceptable for certain types of use cases. Feel free to add capitalization, numbers or special characters as needed to increase the overall passphrase strength.

## Requirements
* [ ] Windows, macOS, Linux, [Pythonista 3](http://omz-software.com/pythonista/) for iPhone
* [ ] [Python](https://www.python.org/downloads/) 3.5 or higher
* [ ] Diceware 8k List File [(Download Here)](http://world.std.com/~reinhold/diceware8k.txt)
* [ ] An Understanding of the Diceware Concept ([XKCD](https://xkcd.com/936/))

Tested on Windows 7 SP1 and Windows 10 x64, Ubuntu Linux 16.04 x64, and macOS 10.12.3.

## Installation
* No installation required. 
* Download dicepy8k.py using [cURL](https://curl.haxx.se/):
```
curl -o dicepy8k.py https://github.com/lotspaih/dicePy8k/raw/master/dicepy8k.py
```

* Download the Diceware 8k file using [cURL](https://curl.haxx.se/):
```
curl -o diceware8k.txt http://world.std.com/~reinhold/diceware8k.txt
```

* Just copy the dicepy8k.py file and the Diceware 8k list file to the same directory on your local computer and run from a command prompt using Python 3.5 or higher.


## Example Use
```
C:\path\to\file\py.exe dicepy8k.py 6
```
or
```
C:\path\to\file\py.exe dicepy8k.py
```
```
How many words do you want for your Diceware passphrase?: 6
```
Results are:
```
Here are your 6 pseudorandom words from the 8k Diceware List:

feel cowman ulan sheik waive nomad

Press any key to continue...
```
*Of course, do not use the words in the above example for an actual passphrase!*

## TODO
* Add command line argument for saving passphrase words (file?, clipboard?)
* Create Windows executable?
* Clean up script (*make it more "[Pythonic](http://docs.python-guide.org/en/latest/writing/style/)"*)

## License and Credit
MIT License for DicePy8k.py

[Diceware](http://world.std.com/~reinhold/diceware.html)
 License Credit
