plain_text=input("Enter the text: ").lower()
key=input("Enter the key: ").lower()

matrix=[[],[],[],[],[]]
s=set()
l=len(key)
r=0
c=0
for ch in key:
	if ch not in s:
		if ch=='i'or ch=='j':
			matrix[r].append("i")
			s.add('i')
			s.add('j')
		else :
			matrix[r].append(ch)
			s.add(ch)
	if len(matrix[r])==5:
		r+=1
for i in range(0,26):
	ch=chr(i+97)
	if ch not in s:
		if (ch=='i' or ch=='j') and 'i' not in s and 'j' not in s:
			matrix[r].append("i")
			s.add('i')
			s.add('j')
		else :
			matrix[r].append(ch)
			s.add(ch)
	if len(matrix[r])==5:
		r+=1

print(f"matrix formed:  {matrix}")

print("Pre_Processing the plain_text!")

new_pt=''
ind=0
while ind<len(plain_text):
	new_pt+=plain_text[ind]
	if ind+1<len(plain_text) and plain_text[ind]==plain_text[ind+1]:
		new_pt+='x'
		ind+=1
		continue
	if ind+1<len(plain_text): 
		new_pt+=plain_text[ind+1]
	ind+=2

if len(new_pt)%2==1:
	new_pt+='x'

print(f"PreProcessed Plaintext: {new_pt}")

def rc(matrix,ch):
	if ch=='i' or ch=='j':
		ch='i'
	for i in range(0,5):
		for j in range(0,5):
			if matrix[i][j]==ch:
				return i,j
	return -1,-1

print("Performing encryption: ")

cipher_text=''
for ind in range(0,len(new_pt),2):
	i1,j1=rc(matrix,new_pt[ind])
	i2,j2=rc(matrix,new_pt[ind+1])

	if i1==i2:
		cipher_text+=matrix[i1][(j1+1)%5]
		cipher_text+=matrix[i1][(j2+1)%5]

	elif j1==j2:
		cipher_text+=matrix[(i1+1)%5][j1]
		cipher_text+=matrix[(i2+1)%5][j2]

	else:
		cipher_text+=matrix[i1][j2]
		cipher_text+=matrix[i2][j1]

print(f"Cipher Text is: {cipher_text}")

print("Performing decryption: ")

plain_text=''
for ind in range(0,len(new_pt),2):
	i1,j1=rc(matrix,cipher_text[ind])
	i2,j2=rc(matrix,cipher_text[ind+1])
	if i1==i2:
	    plain_text+=matrix[i1][(j1-1)%5]
	    plain_text+=matrix[i1][(j2-1)%5]

	elif j1==j2:
		plain_text+=matrix[(i1-1)%5][j1]
		plain_text+=matrix[(i2-1)%5][j2]

	else:
		plain_text+=matrix[i1][j2]
		plain_text+=matrix[i2][j1]
	

print(f"plain Text from cipher text is: {plain_text}")






