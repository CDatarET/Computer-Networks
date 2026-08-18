print("Enter base IP address: ", end="")

ip = input().split(".")

for i in range(len(ip)):
    ip[i] = int(ip[i])

print("Enter CIDR prefix: /", end="")

cidr = int(input())

if cidr < 24 or cidr > 30:
    print("Error: This program currently supports Class C subnetting (CIDR 24 to 30).")
    exit()

hostBits = 32 - cidr

blockSize = 2 ** hostBits

subnets = 256 // blockSize

usableHosts = blockSize - 2

lastOctetMask = 256 - blockSize

print("--- General Subnet Information ---")

print("Calculated Subnet Mask : 255.255.255." + str(lastOctetMask))
print("Total Usable Hosts     : " + str(usableHosts) + " per subnet")
print("Total Subnets Created  : " + str(subnets))

for i in range(subnets):

    networkOctet = ip[3] + (i * blockSize)
    broadcastOctet = networkOctet + blockSize - 1

    firstHostOctet = networkOctet + 1
    lastHostOctet = broadcastOctet - 1

    print("\nSubnet " + str(i + 1))
    print("Network Address   : " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(networkOctet))
    print("First Host        : " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(firstHostOctet))
    print("Last Host         : " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(lastHostOctet))
    print("Broadcast Address : " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(broadcastOctet))