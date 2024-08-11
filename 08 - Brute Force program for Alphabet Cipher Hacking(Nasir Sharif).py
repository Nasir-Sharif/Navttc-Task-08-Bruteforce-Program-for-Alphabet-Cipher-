alphabet = [chr(i) for i  in range(97,123)] * 4
def caesear(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text
def brute_force_caesar(cipher_text):
    print("Brute Force Results:")
    for shift in range(100):
        decoded_text = caesear(start_text=cipher_text, shift_amount=shift, cipher_direction="decode")
        print(f"Shift amount {shift}: {decoded_text}")

cipher_text = input("Enter the cipher text to brute force:\n").lower()
brute_force_caesar(cipher_text)


