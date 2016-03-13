from abc import ABCMeta, abstractmethod

class CipherInterface(metaclass=ABCMeta):
	#not exactly sure this is how to implement an interface
	def __init__(self):
		self.key = ""

	def setKey(self, keyString):
		pass

	def encrypt(self, plaintext):
		pass

	def decrypt(self, ciphertext):
		pass