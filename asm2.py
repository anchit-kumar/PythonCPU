def to_eight_digit_binary(n):
    binary_str = bin(n)[2:]
    return binary_str.zfill(8)

with open('./program.asm', 'r') as asm_file:
    asm_lines = asm_file.readlines()
asm_file.close()

addrValStore = [] #Each elm has form of [lineNumber, data]
for line in asm_lines:
    line = line.strip().split()
    if(line[0]=='data'):
        addrLine = line[1].split(",")
        addrValStore.append(to_eight_digit_binary(int(addrLine[1]))) 

#print(addrValStore)

with open('./mem/program.mem','a') as program_mem:
    for i in range(len(addrValStore)):
        program_mem.write(addrValStore[i]+"\n")

program_mem.close()