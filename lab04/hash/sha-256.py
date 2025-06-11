import hashlib


def calculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Nhap du lieu can bam")
hash_value = calculate_sha256(data_to_hash)
print("Gia tri hash sha256:", hash_value)







