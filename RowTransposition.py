from CipherInterface import CipherInterface
import math

class RowTransposition(CipherInterface):
	def __init__(self):
		self.key = []
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def setKey(self, keyString):
		self.key = keyString.split()
		sortedKey = sorted(self.key)
		count = 1
		for keyPart in sortedKey:
			if int(keyPart) != count:
				return False
			count += 1
		return True

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
		pass