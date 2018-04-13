#!/usr/bin/env python
import sys
import imp
try:
    imp.find_module('pycipher')
    found = True
except ImportError:
    found = False
if (found == True):
    from pycipher import Vigenere as v
if (found == False):
    print ("Library pycipher no found. Please install with 'pip install pycipher'")

args=sys.argv[::]
argtotal=int(len(sys.argv[::]))
key=str
text=str

class vign():
    def ecipher(self, key, text):
        out=v(key).encipher(text)
        print (out)
        
    def dcipher(self, key, text):
        out=v(key).decipher(text)
        print (out)
        
class help():
    def helpone():
        flagk=str
        flagt=str
        flage=str
        flagd=str

        if (args[1] == "--help"):
            print ('Syntax: vigenere.cipher -e or -d -k "keycipher" -text "texttocipher"')
            print ('-k - Reference to key for cipher your text')
            print ('-text - Text to cipher')
            print ('-e - Mode Cipher')
            print ('-d - Mode Decipher')
            exit()
        for i in range(0, len(args)):
        
            if (args[i] == "-k"):
                flagk=str(args[i])
                key=str(args[i+1])
                
	    if (args[i] == "-e"):
	    	flage=str(args[i])
	    	
	    if (args[i] == "-d"):
	    	flagd=str(args[i])
	    	
            if (args[i] == "-text"):
                flagt=str(args[i])
                text=str(args[i+1])
                
        if (flagk != "-k"):
            print("Please inform a key with -k 'key'")
            
	if (flagt != "-text"):
	    print("Please inform a text to cipher with -text 'text'")
	    
	if (flage != "-e"):
	    if (flagd != "-d"):
    	        print("Please inform type: -d for decipher or -e for cipher")
    	        exit()
    	elif (flage == "-e"):
    	    result=vign().ecipher(key, text)
    	    
	if (flagd != "-d"):
	    if (flage != "-e"):
    	        print("Please inform type: -d for decipher or -e for cipher")
    	        exit()
    	elif (flagd == "-d"):
    	    result=vign().dcipher(key, text)
    if (argtotal == 1):
        print("For more information: --help")
    else:
        helpone()
        
#---------------------------------------------------------------------------

help()
