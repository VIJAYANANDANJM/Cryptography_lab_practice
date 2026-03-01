plain_text=input('Enter the plain text: ')
key=input('Enter the key: ').lower()
l_key=list(key)
l_key.sort()
sort_key=''.join(l_key)

d={}
l=len(key)
for ch in key:
	d[ch]=''

t=-len(plain_text)%l

for _ in range(t):
	plain_text+='x'


ind=0
for ch in plain_text:
	d[key[ind%l]]+=ch
	ind+=1
print(d)



cipher_text=''
for ch in sort_key:
	cipher_text+=d[ch]

print("cipher_text : ",cipher_text)

print(f"key: {key}")

sort_key=''.join(sorted(key))

print(sort_key)

de_new={}
sin=0
upv=len(cipher_text)//len(key)
for ind in range(0,len(cipher_text),upv):
	de_new[sort_key[sin]]=cipher_text[ind:ind+upv]
	sin+=1
print(de_new)

plain_text=''
row=0
for _ in range(upv):
	for ch in key:
		plain_text+=de_new[ch][row]
	row+=1

print(f"Plain_Text from cipher is: {plain_text}")


