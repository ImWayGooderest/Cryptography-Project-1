from CipherInterface import CipherInterface

class Caesar(CipherInterface):
	def __init__(self):
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.key = ""

	def setKey(self, keyString):
		self.key = keyString
		return True

	def encrypt(self, plaintext):
		plaintext = plaintext.upper()
		ciphertext = ""
		for char in plaintext:
			if char in self.alphabet:
				pos = self.alphabet.find(char)
				ciphertext += self.alphabet[(pos + int(self.key)) % 26]

		return ciphertext

	def decrypt(self, ciphertext):
		ciphertext = ciphertext.upper()
		plaintext = ""
		for char in ciphertext:
			if char in self.alphabet:
				pos = self.alphabet.find(char)
				plaintext += self.alphabet[(pos - int(self.key)) % 26]

		return plaintext