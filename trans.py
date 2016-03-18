#list of columns
columns = ["" , "" , "" , "" , "" ]
#p=columns.split()

#the plain text
plaintext = "heisdoinghishomework"
print ("the plain text is ")
print (plaintext)
print ("\n")
#thecolIndex
colIndex = 0

#the key
key = [ 5 , 3 , 1 , 2 , 4]

print ("the plaintext arranged according to Key is \n")
#looping through the string
for alphabet in plaintext:

    #adding alphabets to the column
    columns[colIndex] += alphabet

    #to advance the Index
    colIndex = (colIndex + 1)% 5

#Key
for item in key:
    print (columns[item-1])


print ("\n")
print ("the cipher text is ")
#print (columns)
#delimiter = ''
ciphertext = columns[4] + columns[2] + columns[0] + columns[1] + columns[3]
#print ("\n")
#the ciphertext is
print (ciphertext)
print ("\n")

#length of the ciphertext
print ("Length of the ciphertext is")
print (len(ciphertext))

#Now to decrypt the data .
#Finding depth of each column
depth =  len(ciphertext)/len(key)
print ("Depth of the ciphertext " )
print (depth)

#depth is 4 now I slice the text by 4
one = ciphertext[:4]
two = ciphertext[4:8]
three = ciphertext[8:12]
four = ciphertext[12:16]
five = ciphertext[16:20]


#Reading columns oN THE OUTPUT "HEISDOINGHISHOMEWORK"
cipher = ( three + four + two + five + one )
print ("\n")

#new columns
column = ["","","",""]

#new index
cIndex = 0

#decryption key
dkey = (1,2,3,4)

#looping
for c in cipher:
    column[cIndex] += c

    cIndex=(cIndex+1) % 4

for de in dkey:
    print (column[de-1])

#printing the decrypted message
print ("\n")
print ("The Decrypted message is")
Dcipher = column[0]+column[1]+column[2]+column[3]
print (Dcipher)

