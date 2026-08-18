print("A subnet is a smaller network created by splitting a larger IP network")
print("A subnet mask is a number that tells devices which part of an IP address identifies the network and which part identifies the host")

print("Enter IP Address: ", end = "")
ip = input().split('.')
ip[0] = int(ip[0])

if ip[0] >= 0 and ip[0] <= 127:
    print("Class A")
    print("First Octet Decimal Range: 0-127")
    print("First Octet Binary Range: 0XXXXXXX")
    print("IP Range: 0.0.0.0-255.255.255.255")
    print("Subnet mask: 255.0.0.0")
    hosts = (2 ** 24) - 2
    print("Hosts Per ID Network: " + str(hosts))
    nets = 2 ** 7
    print("Number of Networks: " + str(nets))
elif ip[0] >= 128 and ip[0] <= 191:
    print("Class B")
    print("First Octet Decimal Range: 128-191")
    print("First Octet Binary Range: 10XXXXXX")
    print("IP Range: 128.0.0.0-191.255.255.255")
    print("Subnet mask: 255.255.0.0")
    hosts = (2 ** 16) - 2
    print("Hosts Per ID Network: " + str(hosts))
    nets = 2 ** 14
    print("Number of Networks: " + str(nets))
elif ip[0] >= 192 and ip[0] <= 223:
    print("Class C")
    print("First Octet Decimal Range: 192-223")
    print("First Octet Binary Range: 110XXXXX")
    print("IP Range: 192.0.0.0-223.255.255.255")
    print("Subnet mask: 255.255.225.0")
    hosts = (2 ** 8) - 2
    print("Hosts Per ID Network: " + str(hosts))
    nets = 2 ** 21
    print("Number of Networks: " + str(nets))
elif ip[0] >= 224 and ip[0] <= 239:
    print("Class D (Muticast)")
    print("First Octet Decimal Range: 224-239")
    print("First Octet Binary Range: 1110XXXX")
    print("IP Range: 224.0.0.0-239.255.255.255")
elif ip[0] >= 240 and ip[0] <= 255:
    print("Class E (Experimenal)")
    print("First Octet Decimal Range: 240-255")
    print("First Octet Binary Range: 1111XXXX")
    print("IP Range: 240.0.0.0-255.255.255.255")
else:
    print("Invalid IP Address")