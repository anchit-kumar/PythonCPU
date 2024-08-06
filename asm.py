opCodes = {"LDA":"000", "STA":"001", "HLT":"010", "AND":"011", "NOT":"100", "SHL":"101", "ADD":"110", "SUB":"111"}
address = {"addr1":"01110", "addr2":"01111", 
           "addr3":"10000", "addr4":"10001",
           "addr5":"10010", "addr6":"10011",
           "addr7":"10100", "addr8":"10101",
           "addr9":"10110", "addr10":"10111",
           "addr11":"11000", "addr12":"11001",
           "":"00000"}

with open('./program.asm', 'r') as asm_file:
    asm_lines = asm_file.readlines()
asm_file.close

machine_code = []
for line in asm_lines:
    line = line.strip().split()
    if not line:
        continue
    if line[0] not in opCodes:
        continue
    binary = []
    binary.append(opCodes[line[0]])
    try:
        binary.append(address[line[1]])
    except IndexError:
        binary.append(address[""])
    machine_code.append("".join(binary))

with open('./mem/program.mem', 'w') as program_mem:
    for code in machine_code:
        program_mem.write(f"{code}\n")
program_mem.close()

#print("Machine code has been written to ./mem/program.mem")
