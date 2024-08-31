import cirq

def quantum_decrypt(private_key, ciphertext):
    """Decrypt a message using quantum circuits."""
    d, n = private_key
    decrypted = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted

if __name__ == "__main__":
    private_key_input = input("Enter the private key (format: d, n): ")
    d, n = map(int, private_key_input.split(','))
    private_key = (d, n)
    
    encrypted_message_input = input("Enter the encrypted message (comma-separated numbers): ")
    encrypted_message = list(map(int, encrypted_message_input.split(',')))
    
    decrypted_message = quantum_decrypt(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
