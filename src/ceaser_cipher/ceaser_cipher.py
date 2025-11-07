import string


def caesar_cipher(text, shift):
    # Expanded alphabet: uppercase, lowercase, digits, punctuation, and space
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    result = ""

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            result += alphabet[(idx + shift) % len(alphabet)]
        else:
            result += char  # leave unrecognized characters unchanged
    return result


if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter the shift (use negative to decrypt): "))
    result = caesar_cipher(text, shift)
    print(result)
