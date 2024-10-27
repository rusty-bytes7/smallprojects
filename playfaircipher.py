# This is the Playfair cipher
import numpy as np

def playfair_encrypt(plaintext, key):
    # Remove duplicate letters from key
    result = ""
    seen = list()
    for char in key:
        if char not in seen:
            result += char
            seen.append(char)
    key = list(seen)

    # Add remaining letters of alphabet to a list, excluding 'j'
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    remaining_letters = [char for char in alphabet if char not in key]
    for char in remaining_letters:
        result += char
        key.append(char)
    matrixlist = key

    # Make the 5x5 matrix
    matrix = np.array(matrixlist).reshape(5,5)
    #print(matrix)

    # Split the plaintext into pairs, adding 'x' if needed
    plaintext = plaintext.lower()
    plaintext = plaintext.replace("j", "i")
    plaintext = [char for char in plaintext if char.isalpha()]
    plaintext = "".join(plaintext)
    pairs = []
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i + 2]
        if len(pair) == 1:
            pair += 'x'  # Add padding if only one letter remains
        pairs.append(pair)
    #print("Pairs:", pairs)

    ciphertext = ""  # Initialize once before the loop

    # Process each pair
    for pair in pairs:
        row1, col1, row2, col2 = None, None, None, None  # Reset each pair

        # Locate each letter in the matrix
        for i in range(5):
            for j in range(5):
                if matrix[i, j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i, j] == pair[1]:
                    row2, col2 = i, j
                if row1 is not None and row2 is not None:
                    break
            if row1 is not None and row2 is not None:
                break

        # Ensure both letters are found
        if row1 is None or row2 is None:
            raise ValueError(f"Could not find both letters in pair {pair}.")

        # Same Row: Shift each letter to the right
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
            newletter1 = matrix[row1][col1]
            newletter2 = matrix[row2][col2]

        # Same Column: Shift each letter down
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
            newletter1 = matrix[row1][col1]
            newletter2 = matrix[row2][col2]

        # Rectangle: Swap columns
        else:
            newletter1 = matrix[row1][col2]
            newletter2 = matrix[row2][col1]

        # Append each new letter to the ciphertext string
        ciphertext += newletter1 + newletter2

    # Print the final result
    print(ciphertext)

plaintext = "heyhihello"
key = input("Enter the key: ")
playfair_encrypt(plaintext, key)

