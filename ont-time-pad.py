import random



plain_text=input("Enter the plain text: ")

def key_generation(plain_text):
	key=''
	for ch in plain_text:
		key+= chr(random.randint(97,97+25))
	return key

key = key_generation(plain_text)

print(f"Plain_text: {plain_text}\nkey generated: {key}")

def en_de(text,key):
	new=''
	for ind in range(0,len(text)):
		new+=chr(ord(text[ind])^ord(key[ind]))
	return new
cipher_text=en_de(plain_text,key)
print(f"Cipher text : {cipher_text.encode().hex()} ")

plain_text_dec=en_de(cipher_text,key)

print(f"Decrypted Plain_text: {plain_text_dec}")

