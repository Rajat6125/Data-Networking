import time

# Display header
print("***********************************************************************************************************************************")
print(f"{'DATA COMMUNICATION AND NETWORKING': ^131}")
print("***********************************************************************************************************************************", "\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'APPLICATION LAYER': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

# Application Layer - Message Input
data = input("MESSAGE:   ")
sendermac = "6E:1A:2B:3C:4D:5E"
recivermac = "5E:3B:2B:7C:4A:5E"
print("Sender's Message : ", data, '\n')
print("Sender's MAC address  : ", sendermac)
print("Receiver's MAC address: ", recivermac)

# delay1 ****************
time.sleep(4)

# Binary conversion
print(f"{'BINARY CONVERSION':-^131}")
data1 = ''.join(format(ord(char), '08b') for char in data)
print(f"Data stream: {data1}")
datax = data1.split()

print("\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'DATA LINK LAYER': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

# Framing process code for data link layer.
print(f"{'FRAMING PROCESS':-^131}", '\n')
datadd1 = ' '.join(format(ord(char), '08b') for char in data)
Datadd1 = datadd1.split(" ")
print(datadd1, '\n', '\n')

datadd1f = []
for i in Datadd1:
    Datadd1[Datadd1.index(i)] = str(len(i)) + i
    datadd1f.append(format(len(i), '08b') + i)
print("FRAMED DATA: ", Datadd1)
print("FINAL DATA AFTER FRAMING:    ", datadd1f, '\n', '\n')

time.sleep(3)

# CHECKSUM FOR ERROR DETECTION
print(f"{'CHECKSUM CALCULATION':-^131}", '\n')

def checkbin(x):
    sum = 0
    for i in x:
        sum += int(i, 2)
    val = bin(sum)[2:]
    return val

addbin = checkbin(datadd1.split(" "))

def check(a1):
    checksum = ""
    for i in a1:
        if i == "0":
            checksum += "1"
        else:
            checksum += "0"
    return [checksum]

CHECKSUM = check(addbin)
print("BINARY SUM VALUE :", addbin)
print(f"CHECKSUM VALUE  : {check(addbin)}")
print('\n', '\n')

time.sleep(3)

# BIT STUFFING PROCESS WILL START AFTER FRAMING PROCESS
print(f"{'BIT STUFFING':-^131}", '\n')

flag = '01111110'

def bit_stuff(data):
    BIT = ""
    one = 0
    for i in data:
        for j in i:
            BIT += j
            if j == "1":
                one += 1
            else:
                one = 0
            if one == 5:
                BIT += '0'
                one = 0
        BIT += " "
    return BIT.strip()

# Example usage:
data = "111110111011111"  # A sample bit stream
stuffed_data = bit_stuff(data)
print(f"Original data: {data}")
print(f"Stuffed data: {stuffed_data}")

BITDATA = bit_stuff(datadd1f)
print("FRAMED DATA", datadd1f)
print("BIT STUFFED FRAMED DATA", BITDATA)
print('\n', '\n')
time.sleep(3)

print("\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'PHYSICAL LAYER': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

print(f"{'DATA FOR TRANSMISSION':-^131}", '\n')

def hexa(z):
    z1 = z.replace(":", "")
    bin_mac = bin(int(z1, 16))[2:].zfill(48)
    return [bin_mac]

dataz = []
dataz.append([hexa(sendermac), hexa(recivermac)])
dataz.append(BITDATA.split(" "))
dataz.append(CHECKSUM)
print(dataz)
print("___________________________________________________________________________________________________________________________________", '\n')

# ------------------------------------------------------------
# Network Layer - Example: IP Addressing
print("\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'NETWORK LAYER (IP)': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

# IP addressing (simplified)
source_ip = "192.168.1.1"
destination_ip = "192.168.1.2"
print(f"Source IP Address: {source_ip}")
print(f"Destination IP Address: {destination_ip}")

# Routing Protocol Example (simplified)
routing_protocol = "RIP (Routing Information Protocol)"
print(f"Routing Protocol: {routing_protocol}")
print("\n", "------------------------------------------------------------")

# ------------------------------------------------------------
# Transport Layer - Example: TCP/UDP
print("\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'TRANSPORT LAYER (TCP/UDP)': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

# Example of TCP/UDP (simplified)
transport_protocol = "TCP"  # Could be "UDP" as well
source_port = 12345
destination_port = 80
print(f"Transport Protocol: {transport_protocol}")
print(f"Source Port: {source_port}")
print(f"Destination Port: {destination_port}")
print("\n", "------------------------------------------------------------")

# ------------------------------------------------------------
# Session Layer - Example: Session establishment
print("\n", "\n")
print("___________________________________________________________________________________________________________________________________")
print(f"{'SESSION LAYER': ^131}")
print("___________________________________________________________________________________________________________________________________", "\n")

# Session Management Example (simplified)
session_id = 1234
print(f"Session ID: {session_id}")
print(f"Session Established Between: {sendermac} and {recivermac}")

print("___________________________________________________________________________________________________________________________________", '\n')

# End of program
