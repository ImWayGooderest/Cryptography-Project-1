#MonoAlphabetic Key
mono = { ' ' :' ', 'a':'f' ,'b':'h' ,'c':'v' ,'d':'g' ,'e':'w' ,'f':'q' ,'g':'p' ,'h':'o' ,'i':'r' ,'j':'e' ,
         'k':'n' ,'l':'s' ,'m':'u' ,'n':'a' ,'o':'b' ,'p':'j' ,'q':'m' ,'r':'y' ,'s':'z' ,'t':'x' ,'u':'c' ,'v':'d' ,'w':'t' ,'x':'i' ,'y':'k' ,'z':'l', '?':'' }

#plaintext for this problem
plaintext = "he is doing his homework"
print ("the Plaintext is :")
print (plaintext)
print ("\n")

#To initiate empty string
encrypt = []

#loop for every letter of plaintext
for item in plaintext:
    encrypt.append(mono[item])

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
#to store items after reverting the mono set
reverse = {}

#loop to reverse the string
for k,v in mono.items():
    reverse[v] = k

#loop to append reverse's itemset to decrypt's stringset
for item in ciphertext:
    decrypt.append(reverse[item])

#print title
print ("the decrypted message is :")
#http://www.pythonlearn.com/html-008/cfbook009.html reference
#joining strings in a list
delimit = ' '
dcipher = delimit.join(decrypt)

#printing deciphered message
print (dcipher)




