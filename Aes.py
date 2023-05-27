from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return cipher.iv + ciphertext

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')
# Anahtar ve metin
key = get_random_bytes(16)
plaintext = input("Şifrelenecek metni giriniz....:")

# Şifreleme
ciphertext = aes_encrypt(key, plaintext)
print("Şifrelenmiş Metin: ", ciphertext)

# Çözme
decrypted_text = aes_decrypt(key, ciphertext)
print("Çözülen Metin: ", decrypted_text)
