from CipherInterface import CipherInterface


class Railfence(CipherInterface):
    def __init__(self):
        self.key = ""

    def setKey(self, keyString):
        self.key = int(keyString)
        return True

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "")
        ciphertext = []
        myindex = 0
        intplain = len(plaintext)
        for i in range(0, self.key):
            ciphertext.append("")

        for i in range(0, intplain):
            ciphertext[myindex] += plaintext[i]
            myindex = (myindex + 1) % self.key

        return "".join(ciphertext)

    def decrypt(self, ciphertext):
        plaintextResult = ""
        rails = self.key
        cipherLen = len(ciphertext)
        col = cipherLen // rails
        extra = cipherLen % rails
        plaintext = []
        temp = 0
        '''for i in range(0, rails):
            plaintext.append("")'''

        plaintext = ["" for i in range(cipherLen)]

        ###print(plaintext)

        if extra > 0:
            for i in range(0, extra):
                plaintext[i] = ciphertext[0:(col + 1)]
                ciphertext = ciphertext[(col + 1):]

            for i in range(extra, rails):
                plaintext[i] = ciphertext[0: col]
                ciphertext = ciphertext[(col):]
                ###print(plaintext)

            test = 0
            for i in range(0, col+1):
                for j in range(0, rails):
                    plaintextResult += plaintext[j][i]
                    if(test == cipherLen - 1):
                        break
                    test += 1
                    ####print(plaintextResult)

            ####print(plaintextResult)

            return plaintextResult
        else:
            for i in range(0, rails):
                plaintext[i] = ciphertext[0: col]
                ciphertext = ciphertext[(col):]
                ###print(plaintext)

            breakNum = 0
            for i in range(0, col):
                for j in range(0, rails):
                    plaintextResult += plaintext[j][i]
                    if(breakNum == cipherLen - 1):
                        break
                    breakNum += 1
                    ###print(plaintextResult)

            return plaintextResult
