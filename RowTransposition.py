from CipherInterface import CipherInterface

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
		plaintext = plaintext.replace('\n', '')
		plaintext = plaintext.replace(" ", "")
		plainLen = len(plaintext)
		print(plainLen)
		keyLen = ''.join(self.key)
		keyLen = len(keyLen)
		counter = 0

		for i in range(0, keyLen):
			if plainLen % keyLen != 0:
				counter += 1
				print(counter)

		print(counter)

		return

	def decrypt(self, ciphertext):
		keyLen = self.key[0]
		keyLen = len(keyLen)
		print(keyLen)
		rows = len(ciphertext)//keyLen
		print(rows)
		plainmatrix = []
		plaintext = []
		print("Lol: " + str(0%3))
		plainmatrix = ["" for i in range(len(ciphertext))]
		tempmatrix = ["" for i in range(len(ciphertext))]
		i = 0

		for i in range(0, keyLen):
			plainmatrix[i] = ciphertext[0:(rows)]
			ciphertext = ciphertext[rows:]




		print(plaintext)
		strKey = self.key[0]
		print(strKey)
		print(plainmatrix)







