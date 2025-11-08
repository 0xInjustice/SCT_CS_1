import os

from cipher_logic import caesar_cipher


def encrypt_decrypt_file(input_path: str, shift: int, mode: str) -> str:
    if not os.path.isfile(input_path):
        raise FileNotFoundError("File not found.")

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = caesar_cipher(content, shift)

    base, ext = os.path.splitext(input_path)
    suffix = f"_{mode}ed"
    output_path = f"{base}{suffix}{ext}"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    return output_path
