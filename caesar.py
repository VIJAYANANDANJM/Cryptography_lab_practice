def ceasar(text,k,type):
	if(type.lower()=="decryption"):
		k=-k;
	new=""
	for ch in text:
		v=65
		if ch.islower():
			v=97
		new+= chr((ord(ch)-v+k)%26+v)
	return new




plain_text=input("Enter a text to encrypt: ") 
print(f"Plait_text : {plain_text}")
cipher_text=ceasar(plain_text,25,"encryption")
print(f"Encrypted Plain_text: {cipher_text}")
print(f"Decrypted Plain_text: {ceasar(cipher_text,25,"decryption")}")

print("Performing a brute Force attack on Cipher_text",end='\n')

for k in range(1,26):
	new=''
	for ch in cipher_text:
		v=65
		if ch.islower():
			v=97
		new+= chr((ord(ch)-v-k)%26+v)
	print(f"For shift value of {k} : Decrypted Plain_text: {new}",end='\n')




