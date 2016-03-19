#MonoAlphabetic Key
mono = { ' ' :' ', 'a':'f' ,'b':'h' ,'c':'v' ,'d':'g' ,'e':'w' ,'f':'q' ,'g':'p' ,'h':'o' ,'i':'r' ,'j':'e' ,
         'k':'n' ,'l':'s' ,'m':'u' ,'n':'a' ,'o':'b' ,'p':'j' ,'q':'m' ,'r':'y' ,'s':'z' ,'t':'x' ,'u':'c' ,'v':'d' ,'w':'t' ,'x':'i' ,'y':'k' ,'z':'l', '!':'?' }

#plaintext for this problem
plaintext = "Vegeta is better than Goku!!"
print ("the Plaintext is :")
print (plaintext)
print ("\n")

#To initiate empty string
encrypt = []

#loop for every letter of plaintext
for item in plaintext:
    encrypt.append(mono[item.lower()])
    #got the lower() just because it had errors when I had plaintext with capitol letters

#print title
print ("the ciphertext is :")
#http://www.pythonlearn.com/html-008/cfbook009.html reference
#joining strings in a list
delimiter=' '

#assigning value to ciphertext
ciphertext = delimiter.join(encrypt)

#print
print (ciphertext)
print("\n")

#initiate Empty string
decrypt = []
#to store new items from the mono set
new = {}

#loop to exchange letters in mono
for k,v in mono.items():
    new[v] = k

#loop to append new's itemset to decrypt stringset
for item in ciphertext:
    decrypt.append(new[item])

#print title
print ("the decrypted message is :")
#http://www.pythonlearn.com/html-008/cfbook009.html reference
#joining strings in a list
delimit = ' '
dcipher = delimit.join(decrypt)

#printing deciphered message
print (dcipher)




