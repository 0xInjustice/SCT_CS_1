# **Caesar Cipher**

A simple Caesar cipher implementation with a graphical user interface (GUI) and file encryption/decryption capabilities.

---

## **Features**

- **Caesar Cipher Logic:** Encrypts and decrypts text using the Caesar cipher algorithm.
- **GUI:** A user-friendly interface built with `tkinter` and `ttkbootstrap` for easy text encryption and decryption.
- **File Encryption/Decryption:** Encrypt or decrypt the contents of a file and save the result to a new file.
- **Copy to Clipboard:** Easily copy the encrypted/decrypted result from the GUI.

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/0xInjustice/SCT_CS_1.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SCT_CS_1
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **GUI**

To run the graphical user interface:

```bash
python src/ceaser_cipher/ceaser_gui.py
```

### **File Encryption/Decryption**

To use the file encryption/decryption script, import the `encrypt_decrypt_file` function from `src.ceaser_cipher.cipher_file`.

**Example:**

```python
from src.ceaser_cipher.cipher_file import encrypt_decrypt_file

# Encrypt a file
encrypt_decrypt_file("my_file.txt", 5, "encrypt")

# Decrypt a file
encrypt_decrypt_file("my_file_encrypted.txt", -5, "decrypt")
```

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
