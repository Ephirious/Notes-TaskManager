from Cryptodome.Cipher import AES
from Cryptodome.Cipher import ChaCha20_Poly1305
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import bcrypt, bcrypt_check


class EncArgumentError(Exception):
    "Wrong encryption/decryption arguments were given"


class EncAuthError(Exception):
    "Can't authenticate data"


def random(size: int) -> bytes:
    """generates random bytes object length of size

    Args:
        size (int): size of returned bytes

    Returns:
        bytes: random bytes
    """
    return get_random_bytes(size)


class ENC:
    """ENC
        class that provides basic encryption and hashing methods
    """
    def __init__(self, alg_init, mode) -> None:
        if alg_init in (AES, ChaCha20_Poly1305):
            self.alg = alg_init
        else:
            raise EncArgumentError
        self.mode = mode

    @staticmethod
    def pass_to_hash(password, salt=None) -> bytes:
        """pass_to_hash
            speaks for itself

        Args:
            password (bytes/str): bytes or string that represent secret key.
            salt (bytes/str, optional): bytes or string that represent \
hashing salt. Defaults to None.


        Returns:
            bytes: secret key hash.
        """
        if isinstance(password, str):
            password = password.encode()
        if salt is None:
            return bcrypt(password, 12)
        if isinstance(salt, str):
            salt = salt.encode()
        return bcrypt(password, 12, salt)

    @staticmethod
    def check_pass(password, pass_hash: bytes) -> bool:
        """chech_pass
            checks if hash was generated from password

        Args:
            password (bytes/str): bytes or string that represent secret key.
            pass_hash (bytes): bytes of hashed secret key\
 (output of pass_to_hash).

        Returns:
            bool: returns True if pass_hash was generated using password,\
 else returns False.
        """
        try:
            if isinstance(password, str):
                password = password.encode()
            bcrypt_check(password, pass_hash)
        except ValueError:
            return False
        return True

    def encrypt(self, data,
                pass_hash: bytes) -> tuple:
        """encrypt
            encrypts data using specific algorithm

        Args:
            data (bytes/str): data that needs to be encrypted.
            pass_hash (bytes): bytes of secret key\
hashed using bcrypt (pass_to_hash).


        Raises:
            EncArgumentError: raised if data format is wrong


        Returns:
            tuple: constists of 4 bytes elements: encrypted data,
            verification tag, encryption nonce, hashed password.
        """
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, bytes):
            pass
        else:
            raise EncArgumentError
        if self.alg is AES:
            cipher = self.alg.new(key=pass_hash[-31:] + b'\0', mode=self.mode)
        elif self.alg is ChaCha20_Poly1305:
            cipher = self.alg.new(key=pass_hash[-31:] + b'\0')
        enc_data, tag = cipher.encrypt_and_digest(data)
        return enc_data, tag, cipher.nonce, pass_hash

    def decrypt(self, enc_data: bytes, tag: bytes, nonce: bytes,
                pass_hash: bytes) -> tuple:
        """decrypt
            decrypts data using specific algorithm


        Args:
            enc_data (bytes/str): encrypted data.
            tag (bytes): verification tag.
            nonce (bytes): encryption nonce.
            pass_hash (bytes, optional): bytes of hashed secret key.\
 Defaults to None.


        Raises:
            EncArgumentError: raised if data format is wrong


        Returns:
            tuple: consists of 2 elements: bytes of decrypted data,\
 bool value that depicts verification result
        """
        if isinstance(enc_data, str):
            enc_data = enc_data.encode()
        elif isinstance(enc_data, bytes):
            pass
        else:
            raise EncArgumentError
        if self.alg is AES:
            cipher = self.alg.new(key=pass_hash[-31:] + b'\0', mode=self.mode,
                                  nonce=nonce)
        elif self.alg is ChaCha20_Poly1305:
            cipher = self.alg.new(key=pass_hash[-31:] + b'\0', nonce=nonce)
        verification = None
        try:
            data = cipher.decrypt_and_verify(enc_data, tag)
            verification = True
        except (KeyError, ValueError):
            verification = False
        return data, verification


class EncChaCha(ENC):
    """EncChaCha
        subclass of ENC provided to use ChaCha20_Poly1305 algorithm

    Args:
        ENC (class): origin class
    """
    def __init__(self) -> None:
        super().__init__(ChaCha20_Poly1305, None)


class EncAES(ENC):
    """EncAES
        subclass of ENC provided to use AES algorithm

    Args:
        ENC (class): origin class
    """
    def __init__(self, mode) -> None:
        super().__init__(AES, mode)
