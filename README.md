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
## If john tool is not installed,use following command for installing.
```bash
sudo apt-get install -y john
```
## Usage

```bash
python3 john.py
```
<img width="649" height="258" alt="johnpass" src="https://github.com/user-attachments/assets/50877745-9e4d-46d5-b11a-28dfe65ed7c0" />

## 📂 Where Are Cracked Passwords Stored?

## After cracking,cracked results are stored in **`john.pot`** inside the **`.john`** folder.

```bash
cd /.john/john.pot
```
```bash
cat john.pot
```
<img width="399" height="64" alt="johnpot" src="https://github.com/user-attachments/assets/d6c53b6d-a0fc-4af4-aad5-a5c6ebff639f" />

## To crack a new hash, delete the old cracked results from the .john folder. Also, delete the hash file where the previous hash was stored.
```bash
rm -rf *
```

<img width="555" height="161" alt="delete" src="https://github.com/user-attachments/assets/4199168a-1f25-4208-9edc-949b15a91525" />
