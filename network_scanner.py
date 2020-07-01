# !/usr/bin/env python

import scapy.all as scapy
import optparse


def scan(ip):
    # send packet
    arp_request = scapy.ARP(pdst=ip)
    # create broadcast
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boradcast = broadcast/arp_request

    # srp send and get response
    '''
        if you did not want to send packet to broadcast 
        you cant add to srp a mac address

        you need to add timeout if no respose move on
        if we did not add timeout and no response 
        the code still running forever :P
    '''
    answared = scapy.srp(arp_request_boradcast, timeout=5, verbose=False)[0]
    clients_list = []

    for element in answared:
        client_dic = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }

        clients_list.append(client_dic)

    return clients_list


def get_target():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest="target",
                      help="Target IP / IP range")
    (options, arguments) = parser.parse_args()
    return options


def print_result(result_list):
    print('IP\t\t\tMAC Address')
    print("-----------------------------------------")

    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_target()
result_list = scan(options.target)
print_result(result_list)


# 172.27.16.1/24
