from CipherInterface import CipherInterface

class Playfair(CipherInterface):
	def __init__(self):
		self.key = ""
		self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
		self.matrix = [[],[],[],[],[]]
		for x in self.matrix:
			for y in range(0, 5):
				x.append('')

	def setKey(self, keyString):
		self.key = keyString.upper()
		self.key = self.key.replace('J', 'I')
		count = 0
		alphCount = 0

		if self.matrix[0][0] != '':		#Clear matrix if not already clear
			for x in range(0, 5):
				for y in range(0, 5):
					self.matrix[x][y] = ''

		for x in range(0, 5):			#Populate Playfair matrix
			for y in range(0, 5):
				if count < len(self.key):
					while count < len(self.key) and self.exists(self.key[count]):
						count += 1
					if count < len(self.key):
						self.matrix[x][y] = self.key[count]
				if count >= len(self.key):
					while alphCount < 25 and self.exists(self.alphabet[alphCount]):
						alphCount += 1
					if alphCount < 25:
						self.matrix[x][y] = self.alphabet[alphCount]
		return True


	def encrypt(self, plaintext):
		plaintext = plaintext.replace(" ","")
		plaintext = plaintext.upper()
		plaintext = plaintext.replace('J', 'I')
		enc = []
		count = 0
		while count < len(plaintext):
			if count == len(plaintext)-1:
				char1 = plaintext[count]
				char2 = 'X'
			else:
				char1 = plaintext[count]
				char2 = plaintext[count+1]

			if char1 == char2:
				char2 = 'X'
				count -= 1
			coord1 = self.getCoord(char1)
			coord2 = self.getCoord(char2)

			if coord1[0] == coord2[0]:
				char1 = self.matrix[coord1[0]][(coord1[1]+1)%5]
				char2 = self.matrix[coord2[0]][(coord2[1]+1)%5]
			elif coord1[1] == coord2[1]:
				char1 = self.matrix[(coord1[0]+1)%5][coord1[1]]
				char2 = self.matrix[(coord2[0]+1)%5][coord2[1]]
			else:
				char1 = self.matrix[coord1[0]][coord2[1]]
				char2 = self.matrix[coord2[0]][coord1[1]]
			enc.append(char1)
			enc.append(char2)

			count += 2
		return "".join(enc)


	def decrypt(self, ciphertext):
		ciphertext = ciphertext.replace(" ","")
		ciphertext = ciphertext.upper()
		ciphertext = ciphertext.replace('J', 'I')
		dec = []
		count = 0
		while count < len(ciphertext):
			
			char1 = ciphertext[count]
			char2 = ciphertext[count+1]

			coord1 = self.getCoord(char1)
			coord2 = self.getCoord(char2)

			if coord1[0] == coord2[0]:
				char1 = self.matrix[coord1[0]][(coord1[1]-1)%5]
				char2 = self.matrix[coord2[0]][(coord2[1]-1)%5]
			elif coord1[1] == coord2[1]:
				char1 = self.matrix[(coord1[0]-1)%5][coord1[1]]
				char2 = self.matrix[(coord2[0]-1)%5][coord2[1]]
			else:
				char1 = self.matrix[coord1[0]][coord2[1]]
				char2 = self.matrix[coord2[0]][coord1[1]]
			dec.append(char1)
			dec.append(char2)

			count += 2
		return "".join(dec)

	def exists(self, target):
		for x in self.matrix:
			for y in x:
				if y == target:
					return True
		return False

	def getCoord(self, target):
		for x in range(0, 5):
			for y in range(0, 5):
				if self.matrix[x][y] == target:
					return [x, y]
