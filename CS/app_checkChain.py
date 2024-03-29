import hashlib

def generate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

# 示例用法
input_string = "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"
sha256_result = generate_sha256(input_string)
print("SHA-256 哈希结果:", sha256_result)
