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
    def pass_to_hash(password, salt) -> bytes:
        """pass_to_hash
            speaks for itself

        Args:
            password (_type_): bytes or string that represent secret key.
            salt (_type_): bytes or string that represent hashing salt.

        Returns:
            bytes: secret key hash.
        """
        if isinstance(password, str):
            password = password.encode()
        if isinstance(salt, str):
            salt = salt.encode()
        return bcrypt(password, 12, salt)

    @staticmethod
    def check_pass(password, pass_hash: bytes) -> bool:
        """chech_pass
            checks if hash was generated from password

        Args:
            password (_type_): bytes or string that represent secret key.
            pass_hash (bytes): bytes of hashed secret key.

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

    def encrypt(self, data: bytes, password=None, salt=None,
                pass_hash=None) -> tuple:
        """encrypt
            encrypts data using specific algorithm

        Args:
            data (bytes): data that needs to be encrypted.
            password (_type_, optional): bytes or string that represent \
secret key. Defaults to None.
            salt (_type_, optional): bytes or string that represent \
hashing  salt. Defaults to None.
            pass_hash (_type_, optional): bytes of hashed secret key. \
Defaults to None.
        Raises:
            EncArgumentError: if given arguments are \
not enough to complete operation.

        Returns:
            tuple: constists of 4 bytes elements: encrypted data,
            verification tag, encryption nonce, hashed password.
        """
        if pass_hash is None:
            pass_hash = self.pass_to_hash(password, salt)
        elif password is None and salt is None and pass_hash is not None:
            pass
        else:
            raise EncArgumentError
        if self.alg is AES:
            cipher = self.alg.new(pass_hash, self.mode)
        elif self.alg is ChaCha20_Poly1305:
            cipher = self.alg.new(pass_hash)
        enc_data, tag = cipher.encrypt_and_digest(data)
        return enc_data, tag, cipher.nonce, pass_hash

    def decrypt(self, enc_data: bytes, tag: bytes, nonce: bytes,
                pass_data: dict) -> tuple:
        """decrypt
            decrypts data using specific algorithm


        Args:
            enc_data (bytes): encrypted data.
            tag (bytes): verification tag.
            nonce (bytes): encryption nonce.
            password (_type_, optional): bytes or string that represents\
 secret key. Defaults to None.
            salt (_type_, optional): bytes or string that represent\
 hashing salt. Defaults to None.
            pass_hash (_type_, optional): bytes of hashed secret key.\
 Defaults to None.

        Raises:
            EncArgumentError: if given arguments are not enough\
 to complete operation.

        Returns:
            tuple: consists of 2 elements: bytes of decrypted data,\
 bool value that depicts verification result
        """
        if "pass_hash" in pass_data:
            pass_hash = pass_data["pass_hash"]
        elif all("password" in pass_data, "salt" in pass_data,
                 "pass_hash" not in pass_data):
            pass_hash = self.pass_to_hash(pass_data["password"],
                                          pass_data["salt"])
        else:
            raise EncArgumentError
        if self.alg is AES:
            cipher = self.alg.new(pass_hash, self.mode, nonce=nonce)
        elif self.alg is ChaCha20_Poly1305:
            cipher = self.alg.new(pass_hash, nonce=nonce)
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
