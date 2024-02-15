import Crypto.Util.number

bits = 1024

# Generar primos para Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo 1 de Alice:", pA, "\n")
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo 2 de Alice:", qA)

# Generar primos para Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("\nPrimo 1 de Bob:", pB)
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo 2 de Bob:", qB)

# Generar claves
nA = pA * qA
print("\nClave pública de Alice:", nA)
nB = pB * qB
print("Clave pública de Bob:", nB)

# Calcular phi
phiA = (pA - 1) * (qA - 1)
print("\nPhi de Alice:", phiA)
phiB = (pB - 1) * (qB - 1)
print("Phi de Bob:", phiB)

# Calcular e, cuarto primo de Fermat
e = 65537

# Calcular d
dA = Crypto.Util.number.inverse(e, phiA)
print("\nClave privada de Alice:", dA)
dB = Crypto.Util.number.inverse(e, phiB)
print("Clave privada de Bob:", dB)

# Cifrado de mensaje
mensaje = "Hola, Bob!"
print("\nMensaje:", mensaje)
print("Longitud del mensaje en bytes:", len(mensaje))
m = int.from_bytes(mensaje.encode(), byteorder='big')
print("Mensaje en bytes:", m)
cM = pow(m, e, nB)
print("Mensaje cifrado:", cM)

# Descifrado de mensaje
dM = pow(cM, dB, nB)
print("\nMensaje descifrado:", dM)
mensaje = dM.to_bytes((dM.bit_length() + 7) // 8, byteorder='big')
print("Mensaje:", mensaje.decode())