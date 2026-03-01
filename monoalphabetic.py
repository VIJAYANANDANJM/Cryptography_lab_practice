import random

def key_generation():
    alphabets='abcdefghijklmnopqrstuvwxyz'
    key=''
    s=set()
    for ch in alphabets:
        while True:
            v=alphabets[random.randint(0,25)]
            if v not in s:
                key+= v
                s.add(v)
                break
    return key

key=key_generation()
print(f"Key generated: {key}")

def encryption(plain_text,key):
    new=''
    plain_text=plain_text.lower()
    for ch in plain_text:
        ind=ord(ch)-97
        new+=key[ind]
    return new

def decryption(cipher_text,key):
    new=''
    for ch in cipher_text:
        v=chr(key.index(ch)+97)
        new+=v 
    return new

plain_text=input("Enter a text: ")

cipher_text=encryption(plain_text,key)

print(f"The Cipher Text is: {cipher_text}")

print(f"The decrypted Text is: {decryption(cipher_text,key)}")






