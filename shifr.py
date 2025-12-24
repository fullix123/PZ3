class CipherDescriptor:
    def __init__(self, cipher_type, shift=0, decrypt=False):
        self.cipher_type = cipher_type
        self.shift = shift
        self.decrypt = decrypt
        self.name = None

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        text = getattr(instance, self.name, "")
        if self.cipher_type == "caesar":
            return self.caesar(text)
        elif self.cipher_type == "atbash":
            return self.atbash(text)

    def __set__(self, instance, value):
        setattr(instance, self.name, value.lower())

    def caesar(self, text):
        result = ""
        shift = -self.shift if self.decrypt else self.shift

        for char in text:
            if char.isalpha():
                pos = ord(char) - ord('a')
                new_pos = (pos + shift) % 26
                result += chr(new_pos + ord('a'))
            else:
                result += char
        return result

    def atbash(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                result += chr(ord('z') - (ord(char) - ord('a')))
            else:
                result += char
        return result

class Cipher:
    caesar_encrypt = CipherDescriptor("caesar", shift=3)
    caesar_decrypt = CipherDescriptor("caesar", shift=3, decrypt=True)

    atbash_encrypt = CipherDescriptor("atbash")
    atbash_decrypt = CipherDescriptor("atbash")


c = Cipher()

c.caesar_encrypt = "hello world"
encrypted = c.caesar_encrypt
print("Цезарь (шифр):", encrypted)

c.caesar_decrypt = encrypted
print("Цезарь (дешифр):", c.caesar_decrypt)

c.atbash_encrypt = "hello world"
encrypted = c.atbash_encrypt
print("Атбаш (шифр):", encrypted)

c.atbash_decrypt = encrypted
print("Атбаш (дешифр):", c.atbash_decrypt)

