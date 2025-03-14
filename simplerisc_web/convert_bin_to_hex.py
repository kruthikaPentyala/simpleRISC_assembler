import sys

def convert_bin_to_hex(bin_file, hex_file):
    with open(bin_file, 'r') as infile, open(hex_file, 'w') as outfile:
        for line in infile:
            hex_value = format(int(line.strip(), 2), '08X')  # Convert binary to hex (8 uppercase hex digits)
            outfile.write(hex_value + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_bin_to_hex.py <binary_input_file> <hex_output_file>")
        sys.exit(1)
    
    binary_input_file = sys.argv[1]
    hex_output_file = sys.argv[2]
    convert_bin_to_hex(binary_input_file, hex_output_file)
