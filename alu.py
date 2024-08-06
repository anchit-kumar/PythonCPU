import mem

def to_eight_digit_binary(n):
    binary_str = n[2:]
    return binary_str.zfill(8)

class Alu:
    memAccses = mem.Memory()
    clock=0
    PC = 0 #Decimal Value
    MAR = 0 #5 bit value
    MDR = 0 #8 bit value
    IR = 0 #3 bit value
    ACC = 0 #8 bit value
    def __init__(self):
        pass

    def start(self):
        memoryArray = Alu.memAccses.memArray
        for i in range(len(memoryArray)):
            Alu.MAR = Alu.PC #T0 RTL
            
            Alu.MDR = memoryArray[Alu.MAR] #T1 RTL
            Alu.PC+=1 #T1 RTL
            
            Alu.IR = Alu.MDR[:3] #T2 RTL
            Alu.IR = int(Alu.IR, 2)
            
            Alu.MAR = Alu.MDR[3:8] #T2 RTL
            
            match Alu.IR:
                case 0:
                    #print("LDA")
                    #print(Alu.MAR)
                    Alu.MDR = memoryArray[int(Alu.MAR, 2)] #T3 RTL
                    Alu.ACC = Alu.MDR #T4 RTL
                case 1:
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    #print("STA")
                    Alu.MDR = Alu.ACC #T3 RTL
                    memoryArray[int(Alu.MAR,2)] = Alu.MDR #T4 RTL
                case 2:
                    #print("HLT")
                    print("Program Halted Succsesfully")
                    exit()
                case 3:
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    #print("AND")
                    Alu.MDR = memoryArray[int(Alu.MAR, 2)] #T3 RTL
                    Alu.ACC = Alu.ACC & Alu.MDR #T4 RTL
                case 4:
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    #print("NOT")
                    Alu.ACC = ~Alu.ACC #T3 RTL
                case 5:
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    #print("SHL")
                    Alu.ACC = Alu.ACC<<1 #T3 RTL
                case 6:
                    #print("ADD")
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    Alu.MDR = memoryArray[int(Alu.MAR, 2)] #T3 RTL
                    #print(Alu.ACC, "Accumulator")
                    Alu.ACC = Alu.ACC+int(Alu.MDR,2) #T4 RTL
                case 7:
                    if(isinstance(Alu.ACC, str)):
                        Alu.ACC = int(Alu.ACC, 2)
                        
                    #print("SUB")
                    Alu.MDR = memoryArray[int(Alu.MAR, 2)] #T3 RTL
                    Alu.ACC = Alu.ACC-int(Alu.MDR,2) #T4 RTLA