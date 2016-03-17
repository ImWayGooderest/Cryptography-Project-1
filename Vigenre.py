from CipherInterface import CipherInterface

class Vigenre(CipherInterface):
	def __init__(self):
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.key = ""

	def setKey(self, keyString):
		self.key = keyString
		return True

	def encrypt(self, plaintext):
		plaintext = plaintext.upper()
		ciphertext = ""
		index = 0
		for char in plaintext:
			if char in self.alphabet:
				pos = self.alphabet.find(char)
				ciphertext += self.alphabet[pos + int(self.key) % 26]
				index

		return ciphertext

	def decrypt(self, ciphertext):
		pass