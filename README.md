# Navttc-Task-08-Bruteforce-Program-for-Alphabet-Cipher-

# Caesar Cipher with Brute Force

## Description

This Python script allows you to decode a Caesar Cipher text by brute-forcing all possible shift values. It prints the results of all shifts, helping you to identify the correct decoded message.

## Code

```python
alphabet = [chr(i) for i in range(97, 123)] * 4

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
```

## Steps

1. **Define the Alphabet List:**
   - Create a list of lowercase letters from `a` to `z` repeated four times to handle shifts beyond the length of the alphabet.

2. **Define the `caesear` Function:**
   - This function performs the Caesar Cipher operation by shifting characters in the `start_text` based on the `shift_amount` and `cipher_direction` (either "encode" or "decode").

3. **Define the `brute_force_caesar` Function:**
   - This function attempts to decode the provided `cipher_text` by trying all possible shift values (from 0 to 99) and prints the decoded results.

4. **Get User Input:**
   - Prompt the user to input the cipher text that needs to be brute-forced.

5. **Call the `brute_force_caesar` Function:**
   - Run the brute force method to decode the input cipher text using all possible shifts and display the results.

## How to Run

1. **Ensure Python is Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script:**
   - Save the provided Python code into a file named `08 - Brute Force program for Alphabet Cipher Hacking(Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `08 - Brute Force program for Alphabet Cipher Hacking(Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 08 - Brute Force program for Alphabet Cipher Hacking(Nasir Sharif).py
     ```

4. **Enter Cipher Text:**
   - Input the cipher text you wish to decode and press Enter.

5. **View Output:**
   - The script will display all possible decoded results with their corresponding shift values.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
