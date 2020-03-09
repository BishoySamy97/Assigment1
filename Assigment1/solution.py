import sys

def Ceasar (type, key, inputf, outputf):
    k = ord(key)
    if(type == 'decrypt'):
        decryptedMsg = ''
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            for i in msg:
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    decryptedMsg += chr(((ord(i)-ord('a')-k+26)%26)+ord('a'))
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    decryptedMsg += chr(((ord(i)-ord('A')-k+26)%26)+ord('A'))
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Decrypted")
            file.write(decryptedMsg)
            file.close()
    elif(type == 'encrypt'):
        encryptedMsg = ''
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            for i in msg:
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    encryptedMsg += chr(((ord(i)-ord('a')+k+26)%26)+ord('a'))
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    encryptedMsg += chr(((ord(i)-ord('A')+k+26)%26)+ord('A'))
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Encrypted")
            file.write(encryptedMsg)
            file.close()


def affine (type, key1, key2, inputf, outputf):
    k1 = ord(key1)
    k2 = ord(key2)
    if(type == 'decrypt'):
        inverseKey = 0
        decryptedMsg = ''
        for i in range(26):
            if(k1*i%26==1):
                inverseKey = i
                break
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            for i in msg:
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    decryptedMsg += chr( (inverseKey*(ord(i)-ord('a')+k2))%26+ord('a') )
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    decryptedMsg += chr( (inverseKey*(ord(i)-ord('A')+k2))%26+ord('A') )
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Decrypted")
            file.write(decryptedMsg)
            file.close()
    elif(type == 'encrypt'):
        encryptedMsg = ''
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            for i in msg:
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    encryptedMsg += chr( (k1*(ord(i)-ord('a')+k2))%26+ord('a') )
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    encryptedMsg += chr( (k1*(ord(i)-ord('A')+k2))%26+ord('A') )
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Encrypted")
            file.write(encryptedMsg)
            file.close()

def Vigenere (type, key, inputf, outputf):
    k = key.lower()
    if(type == 'decrypt'):
        decryptedMsg = ''
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            x = 0
            for i in msg:
                b = key[x%len(key)]
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    shift = ord(b)-ord('a')
                    decryptedMsg += chr( (ord(i)-ord('a')-shift+26)%26+ord('a') )
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    shift = ord(b)-ord('a')
                    decryptedMsg += chr( (ord(i)-ord('A')-shift+26)%26+ord('A') )
                else: decryptedMsg += chr(ord(i))
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Decrypted")
            file.write(decryptedMsg)
            file.close()
    elif(type == 'encrypt'):
        encryptedMsg = ''
        file = open(inputf, 'r')
        if (file.mode == 'r'):
            msg = file.read()
            x = 0
            for i in msg:
                b = key[x%len(key)]
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    shift = ord(b)-ord('a')
                    encryptedMsg += chr( (ord(i)-ord('a')+shift+26)%26+ord('a') )
                elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    shift = ord(b)-ord('a')
                    encryptedMsg += chr( (ord(i)-ord('A')+shift+26)%26+ord('A') )
                else: encryptedMsg += chr(ord(i))
            file.close()
        file = open(outputf, 'w')
        if (file.mode == 'w'):
            print("Encrypted")
            file.write(encryptedMsg)
            file.close()


def main(argv):
    if(argv[1] == "shift"):
        type, inputf, outputf, key = argv[2:]
        Ceasar(type, key, inputf, outputf)
    elif(argv[1] == "affine"):
        type, inputf, outputf, key1, key2 = argv[2:]
        affine(type, key1, key2, inputf, outputf)
    elif(argv[1] == "vigenere"):
        type, inputf, outputf, key = argv[2:]
        Vigenere(type, key, inputf, outputf)
main(sys.argv)
