# IMPORTING REQUIRED LIBRARIES:
# =============================

from cryptography.fernet import Fernet

# ┌─ What does it do?
# │  Fernet is a symmetric encryption tool (same key locks AND unlocks)
# │
# ├─ How does it help?
# │  We use the SAME Fernet object to decrypt what we encrypted before
# │  It knows how to reverse the encryption process
# │
# └─ Why use it?
#    - Creates matching cipher object with correct key
#    - Handles decryption automatically

import base64

# ┌─ What does it do?
# │  Converts binary data into safe text format and vice versa
# │
# ├─ How does it help?
# │  Decryption needs the key in base64 format (same as encryption)
# │  Ensures key is consistent between lock and unlock operations
# │
# └─ Why use it?
#    - Key must be base64-encoded for Fernet to work
#    - Maintains compatibility with encrypted file

import hashlib

# ┌─ What does it do?
# │  Converts passwords into fixed-length encryption keys
# │
# ├─ How does it help?
# │  User enters password → We convert to same key format as encryption
# │  Same password produces same key = Can unlock the file
# │
# └─ Why use it?
#    - CRITICAL: Must produce EXACT same key as encryption
#    - If password matches, key matches, decryption works
#    - If password wrong, key wrong, decryption fails


# THE ACTUAL DECRYPTION PROCESS:
# ===============================

# 1️⃣ Ask for password
password = input("Enter password to unlock file: ")
# PURPOSE: Get the secret passphrase to unlock the file
# HELPING HOW: Only correct password will generate the correct key
#              to decrypt the locked file


# 2️⃣ Generate same key
key = hashlib.sha256(password.encode()).digest()
# ┌─ What happens here?
# │  Takes the password user entered and converts to a key
# │  Uses SHA256 hash (same algorithm as encryption)
# │
# ├─ How does it help?
# │  CRUCIAL: This must produce EXACTLY the same key as encryption
# │  If user entered same password → same hash → same key → decryption works
# │  If user entered wrong password → different hash → different key → fails
# │
# └─ Why important?
#    Encryption: "hello" → [specific 32-byte key] → File locked
#    Decryption: "hello" → [SAME 32-byte key] → File unlocks ✓
#    Decryption: "hello123" → [DIFFERENT key] → File stays locked ✗

key = base64.urlsafe_b64encode(key)
# ┌─ What happens here?
# │  Converts the 32-byte key into base64 text format
# │  Same process as encryption to maintain consistency
# │
# ├─ How does it help?
# │  Fernet requires base64-encoded keys for both encryption AND decryption
# │  This ensures key format matches what Fernet expects
# │
# └─ Why important?
#    Without this, Fernet won't recognize the key and will fail


cipher = Fernet(key)
# ┌─ What happens here?
# │  Creates a decryption machine using your reconstructed key
# │  cipher = Ready-to-use decryption tool
# │
# ├─ How does it help?
# │  Now we have an object that can reverse the encryption
# │  It uses the same key that encrypted the file originally
# │
# └─ Why important?
#    Next step will use this cipher object to unlock the data


# 3️⃣ Read encrypted file
with open("secret.txt", "rb") as file:
    #    └─ "rb" = Read in Binary mode (not text mode)
    #       Why binary? Encrypted data is bytes, not human-readable text
    encrypted_data = file.read()
# ┌─ What happens here?
# │  Opens the locked secret.txt and reads ALL encrypted content
# │  encrypted_data = Contains the jumbled/scrambled file
# │
# ├─ How does it help?
# │  We now have the encrypted garbage that needs to be converted back
# │
# └─ Why "rb" mode?
#    Encrypted file contains binary bytes that shouldn't be text-decoded
#    rb = Raw binary, no interpretation


# 4️⃣ Try to decrypt
try:
    #    └─ "try" block = Attempt this operation
    #       If it fails, don't crash - handle the error gracefully
    decrypted_data = cipher.decrypt(encrypted_data)
    # ┌─ What happens here?
    # │  Cipher uses your key to unscramble the encrypted file data
    # │  JUNK DATA → ORIGINAL TEXT (if key is correct!)
    # │
    # ├─ How does it help?
    # │  Reverses the encryption process completely
    # │  Returns the original readable file content
    # │
    # └─ Why it might fail?
    #    If wrong password entered → wrong key → decryption fails (caught by except)
    #    If file corrupted → decryption fails (caught by except)

    with open("secret.txt", "wb") as file:
        #   └─ "wb" = Write in Binary mode (not text mode)
        #      Why binary? Decrypted data is bytes, same format as original
        file.write(decrypted_data)
    # ┌─ What happens here?
    # │  Takes the decrypted readable data
    # │  Overwrites the encrypted file with original content
    # │  File is now UNLOCKED and readable again
    # │
    # ├─ How does it help?
    # │  File returns to its original state
    # │  You can now read the original message
    # │
    # └─ Result:
    #    [JUNK ENCRYPTED DATA] → "This is my secret message."
    #    Success! 🔓

    print("File unlocked successfully 🔓")
    # Success message - decryption worked!

except:
    #  └─ "except" block = If try block fails, do this instead
    #     This prevents program crash
    print("Wrong password ❌")
# ┌─ What happens here?
# │  If decryption fails, this message displays
# │  Program doesn't crash, just shows error
# │
# ├─ Why this happens?
# │  User entered wrong password → wrong key → cipher.decrypt() failed
# │  Could also mean file is corrupted
# │
# └─ How does it help?
#    User knows immediately that password was wrong
#    Can try again with different password
#    Program remains stable and user-friendly
