import sys
import tty
from microsofttranslator import Translator
from os import system

#credentials for bing api

client_id = "" #write your client id here
client_secret = "" #write your client secret here

client = Translator(client_id, client_secret, debug=False) #contsructs the translate instance

tty.setcbreak(sys.stdin) #logs keystrokes
sentence=[]
while True:
    out = ord(sys.stdin.read(1))
    letter = chr(out)
    print letter,
    sentence.append(letter)    
    if (letter == '.' or letter =='\n' or letter =='?'): # when sentence is over translate and speak
    	output= ''.join(sentence)
    	result = client.translate(output, "nl") #translate to specified language, here it is Dutch
    	speech = 'say   ' + result
    	system(speech)
    	print output + '\n'
    	print result
    	sentence=[]
    	output=''