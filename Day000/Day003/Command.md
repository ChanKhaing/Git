Markdown
# 🌌 The Art of Hiding Secrets: Journey, Grit, and Cryptography

> *"Clap for yourself today. Not because you are done, but because you didn't stop, quit and you are still on the journey."*

This repository is a personal milestone documenting my practical journey through Linux cryptography and steganography. It represents the "grit" of failing multiple times, troubleshooting, and finally mastering the process of securing data inside plain sight.

---

## 🚀 What I Learned & Documented

### 1. Base64 Encoding & Decoding
Understanding how data can be represented in ASCII format. 
* **Decode Command:**
  ```bash
  echo "Q2xhcCBmb3IgeW91cnNlbGYgdG9kYXkuTm90IGJlY2F1c2UgeW91IGFyZSBkb25lLGJ1dCBiZWNhdXNlIHlvdSBkaWRuJ3Qgc3RvcCxxdWl0IGFuZCB5b3UgYXJlIHN0aWxsIG9uIHRoZSBqb3VybmV5Cg==" | openssl enc -base64 -d
2. Symmetric Encryption with OpenSSL (AES-256-CBC)
Moving from basic encoding to real, password-protected encryption. I learned that encrypting raw strings requires proper piping, while file encryption needs dedicated input (-in) and output (-out) flags.

String Encryption Pipeline Test:

Bash
echo "Your Secret Message" | openssl enc -aes-256-cbc -pbkdf2 | openssl enc -base64
File Encryption (The Correct Way):

Bash
openssl enc -aes-256-cbc -pbkdf2 -in secret.txt -out encrypted_secret.enc
3. Steganography with Steghide
The final art piece. Hiding the encrypted file (-ef) inside a beautiful cover file (-cf) like a starry night photo, locked behind a secure passphrase.

Embedding the Secret:

Bash
steghide embed -cf cover_photo.jpg -ef encrypted_secret.enc
Extracting the Secret:

Bash
steghide extract -sf cover_photo.jpg
🎨 The Metaphor of the Cover Photo
The starry night photo used in this project isn't just a cover file; it's a visual representation of Grit.
