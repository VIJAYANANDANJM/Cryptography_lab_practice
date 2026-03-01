import math
import numpy as np
import random
plain_text=input("Enter the plain_text: ")

key_d=int(input("Enter the dimension of the key: "))

key=[]
print("Enter the key: ")
for i in range(0,key_d):
	t=[]
	for j in range(0,key_d):
		t.append(int(input()))
	key.append(t)

print(key)

key=np.array(key)

print(math.gcd(int(np.linalg.det(key)),26))

print("Finding the Cipher text: ")
cipher_text=''
if len(plain_text)%2==1:
	plain_text+='x'
for ind in range(0,len(plain_text),2):
	P=np.array([[ord(plain_text[ind])-97],
		         [ord(plain_text[ind+1])-97]])
	result=np.dot(key,P)
	print(result)
	cipher_text+=chr(result[0,0]%26+97)
	cipher_text+=chr(result[1,0]%26+97)

print(f"Cipher_text: {cipher_text}")







print("Finding the Plain text from cipher_text: ")
plain_text_c=''
key_inv=np.linalg.inv(key)
for ind in range(0,len(cipher_text),2):
	P=np.array([[ord(cipher_text[ind])-97],
		         [ord(cipher_text[ind+1])-97]])
	result=np.dot(key_inv,P)
	plain_text_c+=chr(int(result[0,0])%26+97)
	plain_text_c+=chr(int(result[1,0])%26+97)


print(f"The inverse of the key is : {key_inv}")

print(f"The decrypted cipher text is: {plain_text_c}")






