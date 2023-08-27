import base58
import hashlib

def hex_to_wif(hex_private_key):
    # Add the prefix byte '80' to indicate the mainnet private key
    extended_key = '80' + hex_private_key
    
    # Double SHA-256 hash the extended private key
    first_hash = hashlib.sha256(bytes.fromhex(extended_key)).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    
    # Take the first 4 bytes of the second hash as checksum
    checksum = second_hash[:4]
    
    # Add the checksum to the end of the extended private key
    extended_key += checksum.hex()
    
    # Encode the extended private key with base58 encoding
    wif = base58.b58encode(bytes.fromhex(extended_key)).decode()
    
    return wif

wif = hex_to_wif("7542FB6685F9FD8F37D56FAF62F0BB4563684A51539E4B26F0840DB361E0027C")
# Test output for the above hex: "5JhvsapkHeHjy2FiUQYwXh1d74evuMd3rGcKGnifCdFR5G8e6nH"

print("WIF:", wif)
