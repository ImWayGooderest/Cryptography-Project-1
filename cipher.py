import Railfence, RowTransposition, Playfair, Vigenre,Caesar
import sys

def handleInput(cipherName, inputKey, encDec, inputFile, outputFile):	###function to handle user input
	iFile = open(inputFile).read()
	oFile = open(outputFile, "w")

	if(cipherName == "PLF"):	###Playfair cipher
		myCipher = Playfair.Playfair()
		myCipher.setKey(inputKey)
		if(encDec == "ENC"):
			cipherText = myCipher.encrypt(iFile)
			oFile.write(cipherText)
		else:
			plainText = myCipher.decrypt(iFile)
			oFile.write(plainText)

	elif(cipherName == "RTS"):	###Row Transposition cipher
		myCipher = RowTransposition.RowTransposition()
		myCipher.setKey(inputKey)
		if(encDec == "ENC"):
			cipherText = myCipher.encrypt(iFile)
			oFile.write(cipherText)
		else:
			plainText = myCipher.decrypt(iFile)
			oFile.write(plainText)

	elif(cipherName == "RFC"):	###Railfence cipher
		myCipher = Railfence.Railfence()
		myCipher.setKey(inputKey)
		if(encDec == "ENC"):
			cipherText = myCipher.encrypt(iFile)
			oFile.write(cipherText)
		elif(encDec == "DEC"):
			plainText = myCipher.decrypt(iFile)
			oFile.write(plainText)
			###oFile.write(plainText)
			###print(iFile)
			###print(iFile[(5+1):])
			###print(myCipher.decrypt(iFile))

	elif(cipherName == "VIG"):	###Vigenre cipher
		myCipher = Vigenre.Vigenre()
		myCipher.setKey(inputKey)
		if(encDec == "ENC"):
			cipherText = myCipher.encrypt(iFile)
			oFile.write(cipherText)
		else:
			###plainText = myCipher.decrypt(iFile)
			###oFile.write(plainText)
			print(iFile)
			print(myCipher.decrypt(iFile))

	elif(cipherName == "CES"):	###Caesar cipher
		myCipher = Caesar.Caesar()
		myCipher.setKey(inputKey)
		if(encDec == "ENC"):
			cipherText = myCipher.encrypt(iFile)
			oFile.write(cipherText)
		else:
			plainText = myCipher.decrypt(iFile)
			oFile.write(plainText)


def main():
	#below is for testing the caesar cipher
	'''testKey = 2
	cipher = Railfence.Railfence()
	cipher.setKey(testKey)
	ciphertext = cipher.encrypt("meet me after the toga party")
	print(ciphertext)'''
	##print(cipher.decrypt(ciphertext))

	'''cipherName = sys.argv[1]
	inputKey = sys.argv[2]
	encrypDecryp = sys.argv[3]
	inputFile = sys.argv[4]
	outputFile = sys.argv[5]
	myFile = open(inputFile).read()'''
	if(len(sys.argv) != 6):
		handleInput(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	else:
		print("Invalid number of arguments!")
	'''if(cipherName == "PLF"):
		myCipher = Playfair.Playfair()
		myCipher.setKey(inputKey)'''


if __name__ == "__main__":
	main()