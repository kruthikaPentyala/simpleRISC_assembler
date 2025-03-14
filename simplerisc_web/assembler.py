import re
import sys

# Define opcode mappings for SimpleRISC ISA
OPCODES = {
    "add": "00000", "sub": "00001", "mul": "00010", "div": "00011", "mod": "00100", "cmp": "00101",
    "and": "00110", "or": "00111", "not": "01000", "mov": "01001", "lsl": "01010", "lsr": "01011",
    "asr": "01100", "nop": "01101", "ld": "01110", "st": "01111", "beq": "10000", "bgt": "10001",
    "b": "10010", "call": "10011", "ret": "10100", "hlt": "11111", "end": "11111"
}

REGISTERS = {f"r{i}": format(i, '04b') for i in range(16)}  # 16 registers

# Function to assemble an instruction
def assemble_instruction(instruction, labels, current_address):
    tokens = re.split(r'[ ,]+', instruction.strip())
    if not tokens or tokens[0] == "":
        return ""

    opcode = OPCODES.get(tokens[0])
    if opcode is None:
        raise ValueError(f"Invalid opcode: {tokens[0]}")

    is_immediate = "0"
    rd_bin = "0000"
    r1_bin = "0000"
    r2_bin = "0000"
    imm_bin = "00000000000000"  # 14-bit immediate field

    if tokens[0] in ["add", "sub", "mul", "div", "mod", "and", "or", "lsl", "lsr", "asr"]:
        rd, r1, r2_or_imm = tokens[1], tokens[2], tokens[3]
        rd_bin, r1_bin = REGISTERS[rd], REGISTERS[r1]
        if r2_or_imm in REGISTERS:
            r2_bin = REGISTERS[r2_or_imm]
        else:
            is_immediate = "1"
            imm_bin = format(int(r2_or_imm), '014b')

    elif tokens[0] == "cmp":
        r1, r2_or_imm = tokens[1], tokens[2]
        r1_bin = REGISTERS[r1]
        if r2_or_imm in REGISTERS:
            r2_bin = REGISTERS[r2_or_imm]
        else:
            is_immediate = "1"
            imm_bin = format(int(r2_or_imm), '014b')

    elif tokens[0] == "mov":
        rd, r1_or_imm = tokens[1], tokens[2]
        rd_bin = REGISTERS[rd]
        if r1_or_imm in REGISTERS:
            r1_bin = REGISTERS[r1_or_imm]
        else:
            is_immediate = "1"
            imm_bin = format(int(r1_or_imm), '014b')

    elif tokens[0] in ["ld", "st"]:
        rd, addr = tokens[1], tokens[2]
        rd_bin = REGISTERS[rd]
        imm_bin = format(int(addr), '018b')
        is_immediate = "1"

    elif tokens[0] in ["bgt", "beq"]:
        label = tokens[1]
        if label in labels:
            imm_bin = format(labels[label], '026b')  # Label address as immediate
        else:
            raise ValueError(f"Undefined label: {label}")
        is_immediate = "1"
        return (opcode + is_immediate + imm_bin).zfill(32)

    elif tokens[0] == "b":
        imm_bin = "00000000000000000000000000"  # 26 zeroes for unconditional branch
        is_immediate = "1"
        return (opcode + is_immediate + imm_bin).zfill(32)

    elif tokens[0] in ["hlt", "end", "nop", "ret"]:
        imm_bin = "00000000000000000000000000"  # Ensure 26-bit zero padding
        return (opcode + "1" + imm_bin).zfill(32)


    return (opcode + is_immediate + rd_bin + r1_bin + r2_bin + imm_bin).zfill(32)

# Function to assemble an entire program
def assemble_program(assembly_code):
    machine_code = []
    labels = {}
    current_address = 0
    
    # First pass: Record label addresses
    lines = assembly_code.split("\n")
    for line in lines:
        line = line.split("//")[0].strip()
        if not line:
            continue
        if ":" in line:
            label = line.split(":")[0].strip()
            labels[label] = current_address
        else:
            current_address += 1

    # Second pass: Convert instructions
    current_address = 0
    for line in lines:
        line = line.split("//")[0].strip()
        if not line or ":" in line:
            continue
        try:
            machine_code.append(assemble_instruction(line, labels, current_address))
        except ValueError as e:
            print(f"Error: {e}")
        current_address += 1
    
    return "\n".join(machine_code)

# Read input file and write to output file
def main(input_file, output_file):
    with open(input_file, 'r') as infile:
        assembly_code = infile.read()
    
    machine_code = assemble_program(assembly_code)
    
    with open(output_file, 'w') as outfile:
        outfile.write(machine_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python assembler.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)