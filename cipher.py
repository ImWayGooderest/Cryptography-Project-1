import Playfair,RowTransposition,Railfence, Vigenre, Caesar, Hill

def main():
	#below is for testing the caesar cipher
	testKey = 1
	cipher = Caesar.Caesar()
	cipher.setKey(testKey)
	ciphertext = cipher.encrypt("this is a test")
	print(ciphertext)
	print(cipher.decrypt(ciphertext))

if __name__ == "__main__":
	main()