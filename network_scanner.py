import scapy.all as scapy

def scan(ip):
    #scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)                                        # instance of an arp request packet
    #print(scapy.ls(scapy.ARP()))
    #arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                        # instance of an ethernet packet
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request                           # combines the two packets
    #arp_request_broadcast.show()

    # searches the MAC address of each device within the network
    # and looks for the one that has the ip of the arp_request packet,
    # we configured to search every MAC address by setting up the Ether dst to ff:ff:ff:ff:ff:ff
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP" + "\t\t\t" + "MAC Address" + "\n-----------------------------------------")
    for answer in answered_list:
        # ip address of the client that responded to the arp request
        # mac address of the client with that ip that responded to the arp request
        print(answer[1].psrc + "\t\t" + answer[1].hwsrc)

def main():
    scan("192.168.173.2/24")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
