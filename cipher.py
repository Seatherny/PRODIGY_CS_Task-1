def caesar_cipher(text, key, mode):
    result = ""

    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - key - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + key - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added as is
            result += char

    return result

def main():
    # Get the text from the user
    text = input("Enter the text: ")
    
    # Get the key from the user
    while True:
        try:
            key = int(input("Enter the key (an integer): "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Get the mode from the user
    while True:
        mode = input("Do you want to encrypt or decrypt the text? (enter 'encrypt' or 'decrypt'): ").lower()
        if mode in ['encrypt', 'decrypt']:
            break
        else:
            print("Please enter 'encrypt' or 'decrypt'.")

    # Perform the encryption or decryption
    result = caesar_cipher(text, key, mode)

    # Print the result
    print(f"The {mode}ed text is: {result}")

if __name__ == "__main__":
    main()