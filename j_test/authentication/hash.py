# Hash 計算範例，可以不用理這個檔案

import hashlib

input = input()

sha224 = hashlib.sha224()

sha224.update(input.encode('utf-8'))

hash_digest = sha224.hexdigest()

print(f"SHA-224 Hash: {hash_digest}")

a = f"{hash_digest}"
