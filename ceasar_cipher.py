# AIM : Caesar Cipher Encoder/Decoder on user input(Message) and their desire shift value.

def caesar_cipher(text, shift, mode):
      
    result = ""
    
    
    if mode == 'decrypt':
        shift = -shift  
    
    for char in text:
        
        if char.isupper():
            
            shifted = chr(((ord(char) - 65 + shift) % 26) + 65)
            result += shifted
            
        elif char.islower():
           
            shifted = chr(((ord(char) - 97 + shift) % 26) + 97)
            result += shifted
        else:
            
            result += char
    
    return result

message = input("Enter your message: ")
shift_value = int(input("Enter the shift value (integer): "))
action = input("Choose 'encrypt' or 'decrypt': ").lower()

while action not in ['encrypt', 'decrypt']:
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
    action = input("Choose 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift_value, action)
print(f"\nResult: {output}")
