import hashlib
import random

def hash_string(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    hashed_data = sha256_hash.hexdigest()

    return hashed_data

# 8 bits
a = "10011010"
ha = hash_string(a)
print(ha)

# 1024 bits
b = b'A'*1024
hb = hash_string(b)
print(hb)

def hash_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256_hash.update(chunk)
    hashed_data = sha256_hash.hexdigest()
    return hashed_data

pdf_file_path = '/Users/sergionegroe/Documents/Anáhuac/Semestre 8/Seguridad Informática y análisis forense/RSA_SIAF/SergioNegroe_Firma_SIAF.pdf'
pdf_hash = hash_file(pdf_file_path)
print(pdf_hash)