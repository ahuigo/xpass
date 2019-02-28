from Crypto.Cipher import AES
class AesEcb():
    def __init__(self, key):
        key = key if isinstance(key, bytes) else key.encode()
        self.aes = AES.new(self.pad(key), AES.MODE_ECB)

    def pad(self, data):
        pad_len = (16 - len(data) % 16)
        return data + bytes([pad_len]) * pad_len

    def encrypt(self, data):
        enc = self.aes.encrypt(self.pad(data))
        return enc

    def decrypt(self, data):
        de = self.aes.decrypt(data)
        return (de[:-de[-1]]) # remove padding


if __name__ == '__main__':
    key = 'password'
    text = '数据'
    enc = AesEcb(key).encrypt(text.encode())
    print(enc)
    dec = AesEcb(key).decrypt(enc).decode()
    print(dec)
