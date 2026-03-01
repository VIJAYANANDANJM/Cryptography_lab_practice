import random

# ---------- modular exponentiation ----------
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# ---------- Diffie-Hellman Key Exchange ----------
def diffie_hellman():
    # Public values (can be known by everyone)
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a generator (g): "))

    print("\nPublic values:")
    print("p =", p)
    print("g =", g)

    # Private keys (secret)
    a = random.randint(2, p-2)   # Alice's private key
    b = random.randint(2, p-2)   # Bob's private key

    print("\nPrivate keys (kept secret):")
    print("Alice private key:", a)
    print("Bob private key:", b)

    # Public keys
    A = mod_exp(g, a, p)   # Alice sends this
    B = mod_exp(g, b, p)   # Bob sends this

    print("\nPublic keys exchanged:")
    print("Alice sends:", A)
    print("Bob sends:", B)

    # Shared secret computation
    secret_alice = mod_exp(B, a, p)
    secret_bob   = mod_exp(A, b, p)

    print("\nShared secrets computed:")
    print("Alice computes:", secret_alice)
    print("Bob computes:", secret_bob)

    if secret_alice == secret_bob:
        print("\n✅ Shared secret established!")
    else:
        print("\n❌ Error: secrets do not match")

# -------- RUN --------
diffie_hellman()