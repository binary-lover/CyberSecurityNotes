def get_ascii_value(char):
    if 'a' <= char <= 'z':
        return ord(char)  # Return ASCII value directly for lowercase
    elif 'A' <= char <= 'Z':
        return ord(char)  # Return ASCII value directly for uppercase
    else:
        return None

def ascii_to_alpha(ascii_value):
    if 97 <= ascii_value <= 122:
        return chr(ascii_value)  # Convert back to lowercase
    elif 65 <= ascii_value <= 90:
        return chr(ascii_value)  # Convert back to uppercase
    else:
        return None 

def process_file(file_path):
    decoded_string = ''
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # Read the first line and strip whitespace
        for char in line:
            ascii_value = get_ascii_value(char)
            if ascii_value is not None:  # Check if it's a letter
                if 'a' <= char <= 'z':
                    new_ascii = 219 - ascii_value  # Invert lowercase
                elif 'A' <= char <= 'Z':
                    new_ascii = 155 - ascii_value  # Invert uppercase
                decoded_char = ascii_to_alpha(new_ascii)
                decoded_string += decoded_char
            else:
                # Keep special characters unchanged
                decoded_string += char
        print(decoded_string)

if __name__ == "__main__":
    input_file = 'encrypted.txt'  # Change this to your file name
    process_file(input_file)

