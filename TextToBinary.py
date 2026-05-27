import os
import time

os.system('clear')
print("\033[1;32m===BINARY MATRIX ENCRYPTER ===\033[0m\n")
secret_message="HELLO, MATHERFATHER"

print(f"Original Text : {secret_message}\n")
print(f"Encrypting into Binary Code...")
time.sleep(1.5)


print("\n\033[1;32]")
for char in secret_message:
    binary=format(ord(char),'08b')
    print(f" {char} --> {binary}")
    time.sleep(0.2)

print("\033[0m\n[✔️] Encryption Completed ! Message Secured.")    