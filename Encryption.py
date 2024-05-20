def encrypt(text, shift):
    """Encrypts the given text using the Caesar Cipher algorithm."""
    encrypted_text = ""
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            if char.islower():  # Check if the character is lowercase
                # Encrypt lowercase letter by shifting it by 'shift' positions
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():  # Check if the character is uppercase
                # Encrypt uppercase letter by shifting it by 'shift' positions
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            # Keep non-alphabet characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts the given text using the Caesar Cipher algorithm."""
    decrypted_text = ""
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            if char.islower():  # Check if the character is lowercase
                # Decrypt lowercase letter by shifting it back by 'shift' positions
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():  # Check if the character is uppercase
                # Decrypt uppercase letter by shifting it back by 'shift' positions
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            # Keep non-alphabet characters unchanged
            decrypted_text += char
    return decrypted_text

def main():
    """Main function to take user input and perform encryption or decryption."""
    choice = input("Do you want to encrypt or decrypt? (e/d): ")
    if choice.lower() == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
