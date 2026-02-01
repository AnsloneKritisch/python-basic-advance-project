# 🧩 STEP 0: Install the required magic tool

# Python doesn’t know AES by default.
# We need a helper library called cryptography.

# 📌 Open terminal / CMD and type:
# pip install cryptography


# ✔ Done? Good. Now real magic starts.

# ----------------------------------------------------------

# 📁 STEP 1: Create a test file

# Create a file named:
# secret.txt

# Write inside it:
# This is my secret message.

# 👉 This is what we’ll lock.

# ----------------------------------------------------------

# 🧱 STEP 2: Understand the building blocks (very important)

# Before code, understand this picture in your head:

# TEXT → ENCRYPT → JUNK DATA
# JUNK DATA → DECRYPT → ORIGINAL TEXT


# Now code 👇

# ----------------------------------------------------------

# 🔐 STEP 3: Create file encryption code

# IMPORTING REQUIRED LIBRARIES:
# =============================

from cryptography.fernet import Fernet

# ┌─ What does it do?
# │  Fernet is a symmetric encryption method (same key to lock and unlock)
# │
# ├─ How does it help?
# │  It provides a ready-made encryption tool that uses AES internally
# │  We don't have to build AES from scratch - it's already optimized
# │
# └─ Why use it?
#    - Simple to use
#    - Secure by default
#    - Handles all the complex math behind the scenes

import base64

# ┌─ What does it do?
# │  Converts binary data into text that can be stored/transmitted safely
# │
# ├─ How does it help?
# │  Encryption creates special binary characters that might not save properly
# │  base64 converts these into readable characters (A-Z, a-z, 0-9, +, /)
# │
# └─ Why use it?
#    - Makes encrypted keys compatible with all systems
#    - Prevents data corruption when storing keys

import hashlib

# ┌─ What does it do?
# │  Takes any text and creates a unique fixed-length code (hash)
# │
# ├─ How does it help?
# │  User passwords are random lengths. AES needs fixed-length keys.
# │  hashlib converts any password → fixed 32-byte key
# │
# └─ Why use it?
#    - Converts user passwords into proper encryption keys
#    - Same password always produces same key (consistent)
#    - Different passwords produce different keys (secure)


# THE ACTUAL ENCRYPTION PROCESS:
# ===============================

# 1️⃣ Take password from user
password = input("Enter password to lock file: ")
# PURPOSE: Get the secret passphrase from user
# HELPING HOW: Without password, anyone could decrypt. Password = security


# 2️⃣ Convert password into a key (AES needs a key)
key = hashlib.sha256(password.encode()).digest()
# ┌─ What happens here?
# │  hashlib.sha256() = Creates a unique 64-character hash from password
# │  password.encode() = Converts text password into bytes (numbers)
# │  .digest() = Returns the hash as 32 bytes of binary data
# │
# ├─ Why this step?
# │  User passwords are weak (too short, varied length)
# │  We need exactly 32 bytes for AES-256 encryption
# │  hashlib stretches short passwords into strong keys
# │
# └─ Example:
#    Password: "hello" → Creates a unique 32-byte key
#    Password: "hello123" → Creates a DIFFERENT 32-byte key
#    Same password always creates same key (important for decryption!)

key = base64.urlsafe_b64encode(key)
# ┌─ What happens here?
# │  Takes the 32-byte key and converts to base64 format
# │  base64 = Safe text format for storing/transmitting data
# │
# ├─ Why this step?
# │  Fernet specifically requires base64-encoded keys
# │  This ensures the key can be stored in text files, emails, etc.
# │
# └─ Result:
#    Random binary bytes → Safe text string (no corruption)


# 3️⃣ Create AES object
cipher = Fernet(key)
# ┌─ What happens here?
# │  Creates an encryption machine using your key
# │  cipher = Ready-to-use encryption tool
# │
# ├─ How does it help?
# │  Now we have an object that can encrypt/decrypt data
# │  It "remembers" your key internally
# │
# └─ Why important?
#    Next steps will use this cipher object to lock/unlock data


# 4️⃣ Read the original file
with open("secret.txt", "rb") as file:
    #    └─ "rb" = Read in Binary mode (not text mode)
    #       Why binary? Because we're going to encrypt bytes, not text
    original_data = file.read()
# ┌─ What happens here?
# │  Opens secret.txt and reads ALL content into memory
# │  original_data = Contains the entire file as bytes
# │
# ├─ How does it help?
# │  We now have the data that needs to be encrypted
# │
# └─ Why "rb" mode?
#    Files are ultimately bytes. rb gives us raw bytes without
#    text encoding/decoding complications


# 5️⃣ Encrypt the data
encrypted_data = cipher.encrypt(original_data)
# ┌─ What happens here?
# │  Cipher uses your key to scramble the file data
# │  Unreadable junk → This is the encrypted result
# │
# ├─ How does it help?
# │  Even if someone opens the file, they see garbage
# │  Only someone with correct password can decrypt
# │
# └─ Technical details:
#    - Uses AES-128 encryption internally
#    - Adds authentication token (prevents tampering)
#    - Result is LARGER than original (adds security info)


# 6️⃣ Write encrypted data back
with open("secret.txt", "wb") as file:
    #    └─ "wb" = Write in Binary mode (not text mode)
    #       Why binary? Because encrypted data is bytes, not text
    file.write(encrypted_data)
# ┌─ What happens here?
# │  Takes the encrypted garbage data
# │  Overwrites the original file with it
# │  Original file is now LOCKED
# │
# ├─ How does it help?
# │  File now contains only encrypted data
# │  Original readable content is completely gone
# │  File is effectively "locked" 🔒
# │
# └─ Result:
#    "This is my secret message." → [JUNK ENCRYPTED DATA]
#    Cannot read without correct password


print("File locked successfully 🔒")
# Tells user the operation completed successfully
