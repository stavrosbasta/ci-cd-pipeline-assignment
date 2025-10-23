#!/usr/bin/env python3
"""
Caesar Cipher Implementation
A simple encryption/decryption program using the Caesar cipher technique.
"""

def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher with the given shift value.
    
    Args:
        text (str): The text to encrypt
        shift (int): The number of positions to shift (positive for right shift)
    
    Returns:
        str: The encrypted text
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Shift the character and wrap around using modulo 26
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypt text using Caesar cipher with the given shift value.
    
    Args:
        text (str): The text to decrypt
        shift (int): The number of positions that were shifted during encryption
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def brute_force_decrypt(text):
    """
    Try all possible shifts (0-25) to decrypt the text.
    Useful when the shift value is unknown.
    
    Args:
        text (str): The encrypted text
    
    Returns:
        list: List of tuples containing (shift, decrypted_text)
    """
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        results.append((shift, decrypted))
    return results


def main():
    """
    Main function to run the Caesar cipher program with CLI interface.
    """
    print("=" * 50)
    print("CAESAR CIPHER PROGRAM")
    print("=" * 50)
    print()
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text (with known shift)")
        print("3. Brute force decrypt (try all shifts)")
        print("4. Exit")
        print()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Encryption
            text = input("\nEnter text to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if shift < 0 or shift > 25:
                    print("Error: Shift must be between 0 and 25")
                    continue
                
                encrypted = caesar_encrypt(text, shift)
                print(f"\nOriginal text:  {text}")
                print(f"Encrypted text: {encrypted}")
                print(f"Shift used:     {shift}")
            except ValueError:
                print("Error: Please enter a valid number for shift")
        
        elif choice == '2':
            # Decryption with known shift
            text = input("\nEnter text to decrypt: ")
            try:
                shift = int(input("Enter shift value used for encryption: "))
                if shift < 0 or shift > 25:
                    print("Error: Shift must be between 0 and 25")
                    continue
                
                decrypted = caesar_decrypt(text, shift)
                print(f"\nEncrypted text: {text}")
                print(f"Decrypted text: {decrypted}")
                print(f"Shift used:     {shift}")
            except ValueError:
                print("Error: Please enter a valid number for shift")
        
        elif choice == '3':
            # Brute force decryption
            text = input("\nEnter text to decrypt: ")
            print("\nTrying all possible shifts:")
            print("-" * 50)
            
            results = brute_force_decrypt(text)
            for shift, decrypted in results:
                print(f"Shift {shift:2d}: {decrypted}")
            
            print("-" * 50)
            print("Look for the result that makes sense!")
        
        elif choice == '4':
            # Exit
            print("\nThank you for using Caesar Cipher Program!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()