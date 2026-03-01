import math

p=int(input("Enter a prime no. :"))
q=int(input("Enter a anther prime no. : "))

n=q*p;
etn=(p-1)*(q-1)

#choosing e 
e=1
for i in range(2,etn):
	if math.gcd(i,etn)==1:
		e=i
		break

#modular inverse d
d=1
for i in range(1,etn):
	if (e*i)%etn==1:
		d=i
		break

print(f"e: {e}\nd: {d}\n n: {n}")

plain_text=int(input("Enter a num to encyrpt: "))

cipher_text=pow(plain_text,e,n)

print(f"Cipher text: {cipher_text}")

decrypted_text=pow(cipher_text,d,n)

print(f"Decrypted text : {decrypted_text}")


