# john-hash-cracker
# John Hash Cracker

This is a simple Python script that automates password cracking using **John the Ripper** and the popular `rockyou.txt` wordlist.

## Features
- Takes a hash input from the user
- Saves the hash to a file
- Automatically unzips `rockyou.txt.gz` if necessary
- Runs John the Ripper with NT format
##Cracked password is stored in

```bash
~/.john/john.pot
```
To crack a new hash, delete the old cracked results
## Usage

```bash
python3 john.py
