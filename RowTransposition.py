from CipherInterface import CipherInterface
import math

class RowTransposition(CipherInterface):
	def __init__(self):
		self.key = []

	def setKey(self, keyString):
		self.key = keyString.split()
		sortedKey = sorted(self.key)
		count = 1
		for keyPart in sortedKey:
			if int(keyPart) != count:
				return False
			count += 1


	def encrypt(self, plaintext):
		numberOfCol = len(self.key)
		ciphertext = ""
		plaintext = plaintext.upper()
		plaintextModified = ""
		for char in plaintext:#strip out non alphabetic chars
			if char in self.alphabet:
				plaintextModified += char

		textSize = len(plaintextModified)
		numberOfRow = math.ceil(textSize/numberOfCol)
		plaintextMatrix = [["X" for x in range(numberOfCol)] for x in range(numberOfRow)] #matrix goes matrix[row][col]
		cipherMatrix = [["X" for x in range(numberOfCol)] for x in range(numberOfRow)]
		count = 0

		#fill matrix
		for row in range(0, len(plaintextMatrix)):
			for col in range(0,len(plaintextMatrix[row])):
				if(count < len(plaintextModified)):
					plaintextMatrix[row][col] = plaintextModified[count]
					count += 1
		#shuffle matrix according to
		count = 0
		for i in range(0,len(plaintextMatrix[0])):
			while count < len(plaintextMatrix):
				cipherMatrix[count][i] = plaintextMatrix[count][int(self.key[i])-1]
				ciphertext += plaintextMatrix[count][int(self.key[i])-1]
				count += 1
			count = 0
		return ciphertext

	def decrypt(self, ciphertext):
		self.key = list(filter(None, self.key))		###removing empty spaces and converting filter into list
		keyLen = self.key
		keyLen = len(keyLen)			###finding the number of columns

		rows = len(ciphertext)//keyLen	###calculating the number of rows

		###generating empty string list
		plainmatrix = ["" for i in range(len(ciphertext))]
		tempmatrix = ["" for i in range(len(ciphertext))]
		newmatrix = [["" for i in range(0, keyLen)] for i in range(0, rows)]

		for i in range(0, keyLen):					###putting ciphertext in plainmatrix,
			plainmatrix[i] = ciphertext[0:(rows)]	###depending on key length
			ciphertext = ciphertext[rows:]


		index = 0
		strKey = self.key

		for i in range(0, rows):					###rearranging cipher and placing in tempmatrix
			for j in range(0, keyLen):
				tempmatrix[i] += plainmatrix[j][i]
				index += 1
				if index == 4:
					index = 0

		plainS = ""
		index = 0
		for i in range(0, rows):					###placing cipher letters in correct row and column,
			for j in range(0, keyLen):				###based on the key
				temp = int(strKey[index])
				newmatrix[i][temp-1] += tempmatrix[i][j]
				index += 1
				if index == keyLen:
					index = 0

		for i in range(0, rows):					###plainS becomes our plaintext
			for j in range(0, keyLen):
				plainS += newmatrix[i][j]

		print("Row Transposition Decryption success!")
		return plainS







