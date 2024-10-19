# ENCRYPTION/DECRYPTION TOOL

### DESCRIPTION:

# Encryption System - Part 1

## Overview
This project implements a custom encryption system where input text is encoded using a predefined set of character mappings. The encrypted text is further fragmented, shuffled, and distributed into two files. The encryption is designed to ensure confidentiality and randomness, with a secret key generated for the decryption process.

## Project Structure
- **Encryption_set**: A predefined set of character-to-code mappings used for the initial encryption of text.
- **Main Program**: The `main()` function orchestrates the encryption process by:
  1. Taking input from the user.
  2. Encrypting the input text.
  3. Fragmenting and shuffling the encrypted text.
  4. Distributing the fragments into two separate files stored in `../server` and `../client` directories.
  5. Providing a final secret key for decryption, combining a sequence code and a random triplet code.

## Files and Directories
1. **../server/**: Contains the first half of the encrypted data.
2. **../client/**: Contains the second half of the encrypted data.
3. **README.md**: This documentation file.

## Functions

### 1. `letterSlicer(str)`
- **Purpose**: Splits the input string into individual characters.
- **Parameters**: 
  - `str`: The input text.
- **Returns**: A list of characters.

### 2. `FirstEncryption(array)`
- **Purpose**: Maps each character from the input list to its corresponding encrypted code using `Encryption_set`.
- **Parameters**: 
  - `array`: List of characters to be encrypted.
- **Returns**: A string of the encrypted text.

### 3. `fragmenter(array)`
- **Purpose**: Breaks the encrypted string into random fragments based on the length of the text.
- **Parameters**:
  - `array`: The encrypted string.
- **Returns**: A list of fragments (as dictionaries) with unique IDs.

### 4. `JumboJumbler(array)`
- **Purpose**: Shuffles the list of fragments to add randomness.
- **Parameters**:
  - `array`: List of fragmented dictionaries.
- **Returns**: A shuffled list of fragments.

### 5. `antiSequencer(array)`
- **Purpose**: Adds randomness to the order of fragments and combines them into a single encrypted output.
- **Parameters**:
  - `array`: List of shuffled fragments.
- **Returns**: 
  - `number_sequence`: A code to track the original fragment sequence.
  - `finalCode`: The combined shuffled fragment data.

### 6. `main()`
- **Purpose**: The main function that runs the encryption process, manages input/output, and stores the results in files.
- **Steps**:
  1. Accepts user input for the text to be encrypted.
  2. Passes the text through `letterSlicer()`, `FirstEncryption()`, `fragmenter()`, `JumboJumbler()`, and `antiSequencer()`.
  3. Splits the final encrypted string into two segments and writes them to the server and client files.
  4. Generates and displays the secret key for the user.

## Usage

1. Run the program:
    ```bash
    python3 encryption.py
    ```

2. Input the text you want to encrypt.

3. The program will display a **Secret Key** for decrypting the data and create two files:
   - `../server/<triplet_code>.txt`
   - `../client/<triplet_code>.txt`

4. Store the secret key securely for future decryption.

---

# Encryption System - Part 2: Decryption Process

## Overview
The second part of the project handles the **decryption process**, reversing the encryption steps. Using the provided **secret key**, the system decodes the shuffled fragments, reconstructs the original encrypted message, and finally converts it back into the plaintext input.

## Project Structure
- **Decryption Process**: The `main()` function for decryption does the following:
  1. Reads two encrypted data segments from files based on the **secret key**.
  2. Identifies the sequence in which the fragments were shuffled using the key.
  3. Re-sequences the fragments in their original order.
  4. Decodes the encrypted message using the predefined `Encryption_set`.
  5. Prints the decrypted message to the user.

## Decryption Functions

### 1. `file_key(key)`
- **Purpose**: Extracts the file identification code from the secret key.
- **Parameters**: 
  - `key`: The secret key provided for decryption.
- **Returns**: The triplet file code from the key used to identify the encrypted files.
  
### 2. `sequenceFinder(string, key)`
- **Purpose**: Identifies the sequence of fragment shuffling by analyzing the sequence part of the secret key.
- **Parameters**:
  - `string`: The secret key.
  - `key`: The file code extracted from the secret key.
- **Returns**: A list of fragment IDs representing the correct sequence for reconstruction.

### 3. `codeLister(string)`
- **Purpose**: Breaks down the encrypted message into individual fragments.
- **Parameters**:
  - `string`: The full concatenated encrypted text.
- **Returns**: A list of encrypted fragments.

### 4. `finalEncodeSequencer(sequence, crypt)`
- **Purpose**: Re-sequences the shuffled fragments to match the original order based on the fragment IDs.
- **Parameters**:
  - `sequence`: The list of fragment IDs.
  - `crypt`: The list of encrypted fragments.
- **Returns**: 
  - `final_coded_text`: The full encrypted message after reordering.
  - `count`: The total length of the final encrypted message.

### 5. `Converter(code, count)`
- **Purpose**: Splits the final encrypted message into triplets for decoding.
- **Parameters**:
  - `code`: The final encrypted string.
  - `count`: The length of the final encrypted message.
- **Returns**: A list of triplets (each representing one character in the original text).

### 6. `Decoder(code_list)`
- **Purpose**: Decodes the encrypted triplets back into the original characters using the predefined `Encryption_set`.
- **Parameters**:
  - `code_list`: A list of encrypted triplets.
- **Returns**: The final decoded text (original user input).

### 7. `main()`
- **Purpose**: The main decryption function.
- **Steps**:
  1. Takes the **secret key** from the user.
  2. Reads the corresponding encrypted data segments from the `../server` and `../client` files.
  3. Reconstructs the shuffled sequence using the `sequenceFinder()`.
  4. Reorders the fragments and assembles the full encrypted text using `finalEncodeSequencer()`.
  5. Decodes the encrypted text back to the original plaintext using `Decoder()` and prints the result.

## Usage

1. Run the decryption program:
    ```bash
    python3 decryption.py
    ```

2. Input your **Secret Key** (provided after the encryption process).

3. The program will:
   - Read the encrypted segments from `../server/` and `../client/` directories.
   - Decode and reconstruct the original message.
   - Print the **Decoded Message**.