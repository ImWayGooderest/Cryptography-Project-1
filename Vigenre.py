from CipherInterface import CipherInterface

class Vigenre(CipherInterface):
	def __init__(self):
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.key = ""

	def setKey(self, keyString):
		self.key = keyString.upper()
		return True

	def encrypt(self, plaintext):
		plaintext = plaintext.upper()
		ciphertext = ""
		index = 0
		for char in plaintext:
			if char in self.alphabet:
				pos = self.alphabet.find(char)
				keyPos = self.alphabet.find(self.key[index % len(self.key)])
				ciphertext += self.alphabet[(pos + keyPos) % 26]
				index += 1

		return ciphertext

	def decrypt(self, ciphertext):
		ciphertext = ciphertext.upper()
		plaintext = ""
		index = 0
		for char in ciphertext:
			if char in self.alphabet:
				pos = self.alphabet.find(char)
				keyPos = self.alphabet.find(self.key[index % len(self.key)])
				plaintext += self.alphabet[(pos - keyPos) % 26]
				index += 1

		return plaintext
