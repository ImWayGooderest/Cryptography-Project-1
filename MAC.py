from CipherInterface import CipherInterface

class (CipherInterface):

def __init__(self):
    #plaintext for this problem
    #plaintext ="Vegeta is better than Goku!!"
    self.key = {' ' :' ', 'a':'f' ,'b':'h' ,'c':'v' ,'d':'g' ,'e':'w' ,'f':'q' ,'g':'p' ,'h':'o' ,'i':'r' ,'j':'e' ,
         'k':'n' ,'l':'s' ,'m':'u' ,'n':'a' ,'o':'b' ,'p':'j' ,'q':'m' ,'r':'y' ,'s':'z' ,'t':'x' ,'u':'c' ,'v':'d' ,'w':'t' ,'x':'i' ,'y':'k' ,'z':'l', '!':'?' }

	#def setKey(self, keyString):


def encrypt(self, plaintext):
    plaintext = plaintext.lower()
    print ("the Plaintext is :")
    print (plaintext)
    print ("\n")
    #To initiate empty string
    enc = []
    #loop for every letter of plaintext
    for item in plaintext:
        enc.append(mono[item])
        #print title
        print ("the ciphertext is :")
        #http://www.pythonlearn.com/html-008/cfbook009.html reference
        #joining strings in a list
        delimiter=' '
        #assigning value to ciphertext
        ciphertext = delimiter.join(enc)
        #print
        print (ciphertext)
        print("\n")


def decrypt(self, ciphertext):
	#initiate Empty string
    dec = []
    #to store items to new mono set
    new = {}

    #loop to reverse the letters in the dictionary
    for k,v in mono.items():
        new[v] = k

    #loop to append new itemset to dec's stringset
    for item in ciphertext:
        dec.append(new[item])

        #print title
        print ("the decrypted message is :")
        #http://www.pythonlearn.com/html-008/cfbook009.html reference
        #joining strings in a list
        delimit = ' '
        dcipher = delimit.join(dec)

        #printing deciphered message
        print (dcipher)
