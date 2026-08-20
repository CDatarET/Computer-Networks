#rewritten assignment 2 from C to python for understanding

def placeBit(transmit, pos):
    count = 0
    s = 0
    skip = False
    for i in range(pos, len(transmit)):
        if transmit[i] == '1' and not skip:
            s += 1
        
        count += 1
        
        if count == pos:
            count = 0
            skip = not skip
    
    if s % 2 == 0:
        transmit[pos] = '0'
    else:
        transmit[pos] = '1'

def checkBit(recieved, pos, wrong):
    count = 0
    s = 0
    skip = False
    for i in range(pos, len(recieved)):
        if recieved[i] == '1' and not skip:
            s += 1
        
        count += 1
        
        if count == pos:
            count = 0
            skip = not skip
            
    if s % 2 == 0:
        wrong.append('0')
    else:
        wrong.append('1')

print("Hello World")
print("Enter Data: ", end = "")
data = input()
r = 0
while(pow(2, r) < len(data) + r + 1):
    r += 1

n = len(data) + r + 1
transmit = [0] * n
power = 0
pos = 0
for i in range(n):
    if i == 2 ** power:
        power += 1
        transmit[i] = 'p'
    else:
        transmit[i] = data[pos - 1]
        pos += 1

copyTransmit = transmit[:]
print("".join(transmit[1:]))
for i in range(len(transmit)):
    if transmit[i] == 'p':
        placeBit(transmit, i)

print("".join(transmit[1:]))

print("Enter recieved data: ", end = "")
recieved = '0' + input()
wrong = []
for i in range(len(recieved)):
    if copyTransmit[i] == 'p':
        checkBit(recieved, i, wrong)
print(wrong)
print("".join(transmit[1:]))
print(recieved[1:])
pos = int("".join(wrong)[::-1], 2) - 1
if pos < 0:
    print("There is no error")
else:
    for i in range(pos):
        print(" ", end = "")
    print("^")
    print("This is error bit")
print("There is error at bit " + str(pos + 1))
