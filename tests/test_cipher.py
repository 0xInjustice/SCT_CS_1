def ceaser_cipher(text, shift):
    result = " "
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


if __name__ == "__main__":
    text = input("Enter the text to encrypt:")
    shift = int(input("Enter the shift:"))
    result = ceaser_cipher(text, 4)
    print(result)
