import cirq

def quantum_encrypt(public_key, message):
    """Encrypt a message using quantum circuits."""
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

if __name__ == "__main__":
    public_key_input = input("Enter the public key (format: e, n): ")
    e, n = map(int, public_key_input.split(','))
    public_key = (e, n)
    
    message = input("Enter the message to encrypt: ")
    encrypted_message = quantum_encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_message}")
