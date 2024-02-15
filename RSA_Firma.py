import Crypto.Util.number
import hashlib

bits = 1024

# Generar primos para Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

# Generar primos para Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

# Generar claves
nA = pA * qA
nB = pB * qB

# Calcular phi
phiA = (pA - 1) * (qA - 1)
phiB = (pB - 1) * (qB - 1)

# Calcular e, cuarto primo de Fermat
e = 65537

# Calcular d
dA = Crypto.Util.number.inverse(e, phiA)
dB = Crypto.Util.number.inverse(e, phiB)

# Mensaje original
mensaje = "Hola, Bob!"

# Calcular el hash del mensaje
hash_mensaje = hashlib.sha256(mensaje.encode('utf-8')).digest()
hash_mensaje_bytes = int.from_bytes(hash_mensaje, byteorder='big')

# Firma del hash del mensaje
hash_mensaje_firma = pow(hash_mensaje_bytes, dA, nA)

# Verificar integridad de la firma
hash_mensaje_validacion = pow(hash_mensaje_firma, e, nA)
if hash_mensaje_bytes == hash_mensaje_validacion:
    print("La firma es válida. ✅")
else:
    print("La firma no es válida. ❌")
