#! /usr/bin/env python

from Crypto.Cipher import AES
import hashlib

BS = AES.block_size

def padding_pkcs5(value):
    return str.encode(value + (BS - len(value) % BS) * chr(BS - len(value) % BS))

def get_sha1prng_key(key):
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).digest()
    return ''.join(['%02x' % i for i in signature]).upper()[:32]
# 加密
def encrypt(key:str,value:str) -> str:
    cryptor = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    padding_value = padding_pkcs5(value)  # padding content with pkcs5
    ciphertext = cryptor.encrypt(padding_value)
    return ''.join(['%02x' % i for i in ciphertext]).upper()
# 字符串处理，过滤特殊字符
def padding_zero(value):
    list = []
    for c in value:
        # ascii码范围获取
        if ord(c) > 31 & ord(c) < 127:
            list.append(c)
    return ''.join(list)

def decrypt(key:str, value:str) -> str:
    ''' AES/ECB/NoPadding decrypt '''
    key = bytes.fromhex(key)
    cryptor = AES.new(key, AES.MODE_ECB)
    ciphertext = cryptor.decrypt(bytes.fromhex(value))
    return padding_zero(str(ciphertext, "utf-8"))

if __name__ == '__main__':
    key = '494F503132333435494F503132333435'
    content = 'MTgzMDk4OTA4MjI='
    edb = encrypt(get_sha1prng_key(key),content)
    print(content +'='+ edb)
    test=get_sha1prng_key(key)
    print(test)
    ddb = decrypt(get_sha1prng_key(key),edb)
    print(edb +'='+ ddb)