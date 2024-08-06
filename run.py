import subprocess
import mem
import alu


subprocess.run(['python', './asm.py'])
subprocess.run(['python', './asm2.py'])

MemWriter = mem.Memory()
MemWriter.write()

Alu = alu.Alu()
Alu.start()
