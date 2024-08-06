class Memory:
    memArray = [0]*32
    
    def __init__(self):
        for i in range(32):
            Memory.memArray[i]= '0'*8
    
    def write(self):
        with open("./mem/program.mem", "r") as program_mem:
            lines = program_mem.readlines()
            for i in range(32):
                try:
                    line = lines[i].replace("\n","")
                    Memory.memArray[i] = line
                except IndexError as e:
                    continue
        program_mem.close()
        #print("Wrote program.mem to array!")

    def clear(self):
        with open("./mem/program.mem", "w") as program_mem:
            pass