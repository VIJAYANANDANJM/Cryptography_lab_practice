def caesar(ch,k):
	return chr((ord(ch)-97+k)%26+97)

plain_text=input("Enter the plain text: ")

key=input("Enter the key: ")

def vigenere_encrypt(plain_text,key):
	cipher_text=''
	for ind in range(0,len(plain_text)):
		shift_key=ord(key[ind%len(key)])-97
		cipher_text+=caesar(plain_text[ind],shift_key)
	return cipher_text

def vigenere_decrypt(cipher_text,key):
	plain_text=''
	for ind in range(0,len(cipher_text)):
		shift_key=ord(key[ind%len(key)])-97
		plain_text+=caesar(cipher_text[ind],-shift_key)
	return plain_text

print(f"Plain_text: {plain_text}")
cipher_text=vigenere_encrypt(plain_text,key)
print(f"cipher_text: {cipher_text}")
cv=str([ord(x)-97 for x in cipher_text])
print(f"cipher_text in ascci: {cv}")
print(f"Plain_text from cipher_text: {vigenere_decrypt(cipher_text,key)}")
