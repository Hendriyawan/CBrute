#! /usr/bin/python
#vim : set fileencoding=utf-8: ^[\t\v]*#.*?coding[:=] [\t]* ([-_.a-zA-Z0-9)+]
# 17/04/2017
#Copyright(c) 2017 hendriyawan

import os
import pycolor
color = pycolor.pyColor()

def banner():
	os.system('clear')
	print """
      ________________
     /  _____/ / /_\ )
    /  /____  / /_\ (
    \______/ /______/"""+color.cyan+"RUTE"+color.reset+" (c)2017\n\t"+color.blue+"creared by : "+color.yellow+"hendriyawan"+color.reset+"\n\t"+color.blue+"code name : "+color.yellow+"mr_silent"+color.reset+"\n\t@___Glanex_Dev___\n"
    
def setWindowTitle(title):
	setTitle = 'echo "\033]0;%s\007"' % str(title)
	os.system(setTitle)
	
def decrypt(cipher,keys):
	ciphertext = list(cipher)
	key = int(keys)
	abjad = 'abcdefghijklmnopqrstuvwxyz'
	alphabet = list(abjad)
	Alphabet = list(str.upper(abjad))
	symbol = list("_,.\"@#$%&-+()*':;!?/\<>^={}[]|~")
	plaintext = ''
	
	for p in ciphertext:
		if p in alphabet:
			plaintext += alphabet[(alphabet.index(p)-key)%26]
		if p in Alphabet:
			plaintext += Alphabet[(Alphabet.index(p)-key)%26]
		if p in symbol:
			plaintext += symbol[(symbol.index(p)-key)%(len(symbol))]
		if p == "\n":
			plaintext = plaintext + p
		if p == " ":
			plaintext = plaintext + p
	print(color.proc(" Result : "+color.result(plaintext)))
	
def main():
	banner()
	setWindowTitle("Caesar Brute")
	ciphertext = raw_input(color.proc(" Enter ciphertext : "))
	key = raw_input(color.proc(" Enter max key/shift : "))
	try:
		for i in range(1, int(key)):
			decrypt(ciphertext,i)
	except:
		print ""
		
if __name__ == "__main__":
	main()