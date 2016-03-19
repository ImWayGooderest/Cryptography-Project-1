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

		textSize = len(plaintext)
		numberOfRow = math.ceil(textSize/numberOfCol)
		plaintext = plaintext.upper()
		matrix = [["X" for x in range(numberOfCol)] for x in range(numberOfRow)] #matrix goes matrix[row][col]
		cipherMatrix = matrix
		count = 0

		#fill matrix
		for row in range(0, len(matrix)):
			for col in range(0,len(matrix[row])):
				if(count < len(plaintext)):
					while(plaintext[count] not in self.alphabet and count < len(plaintext)): #skip char if not a letter
						count += 1
					matrix[row][col] = plaintext[count]
					count += 1


	def decrypt(self, ciphertext):
		pass