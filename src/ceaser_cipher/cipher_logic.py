import string


def caesar_cipher(text: str, shift: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    result = []
    mod = len(alphabet)
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            result.append(alphabet[(idx + shift) % mod])
        else:
            result.append(ch)
    return "".join(result)
