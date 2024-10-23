import argparse

def split_string_in_blocks(s):
    blocks = []
    for i in range(0, len(s), 3):
        blocks.append(s[i:i+3])
    return blocks

def shiftOne(block):
    return block[-1] + block[0:2]  # Shift the characters in the block

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().strip()  # Read the content and strip whitespace

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process a string from a file.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the input file')

    args = parser.parse_args()

    # Read the input string from the specified file
    input_string = read_file(args.file)
    blocks = split_string_in_blocks(input_string)

    for i in range(len(blocks)):
        blocks[i] = shiftOne(blocks[i])

    decoded = "".join(blocks)
    print(decoded)

if __name__ == "__main__":
    main()

