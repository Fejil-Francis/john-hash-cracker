import subprocess
import os

hash_input = input("Enter the hash: ")

with open("hash", "w") as f:
    f.write(hash_input + "\n")


if not os.path.exists("/usr/share/wordlists/rockyou.txt"):
    print("Unzipping rockyou.txt.gz...")
    subprocess.run(["gunzip", "/usr/share/wordlists/rockyou.txt.gz"], check=True)


print("Starting password cracking with John...")
subprocess.run([
    "john",
    "--format=NT",
    "--wordlist=/usr/share/wordlists/rockyou.txt",
    "hash"  
], check=True)
