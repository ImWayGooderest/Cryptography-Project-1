import Playfair,RowTransposition,Railfence, Vigenre, Caesar, Hill

def main():
	#below is for testing the caesar cipher
	testKey = 1
	cipher = Caesar.Caesar()
	cipher.setKey(testKey)
	print(cipher.encrypt("this is a test"))

if __name__ == "__main__":
	main()