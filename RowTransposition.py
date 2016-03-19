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

		return True
	def encrypt(self, plaintext):
		pass

	def decrypt(self, ciphertext):
		pass