# 🔐 John Hash Cracker

A simple yet powerful Python script that automates password cracking using **John the Ripper** and the classic `rockyou.txt` wordlist. Perfect for ethical hacking practice and learning how hash cracking works in real-world scenarios.

---

## ⚙️ Features

- 🔑 Accepts a hash input directly from the user
- 📄 Saves the hash into a file for John the Ripper to process
- 📦 Automatically extracts `rockyou.txt.gz` if not already unzipped
- ⚔️ Launches John the Ripper in `--format=NT` mode for cracking
- 🧠 Stores cracked passwords in a persistent `.pot` file for later lookup

---

## 📂 Where Are Cracked Passwords Stored?

After cracking, the results are stored in:

```bash
~/.john/john.pot
```
## To crack a new hash, delete the old cracked results from the .john folder. Also, delete the hash file where the previous hash was stored.
## Usage

```bash
python3 john.py

