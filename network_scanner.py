# !/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boradcast = broadcast/arp_request

    print(arp_request.summary())
    print(broadcast.summary())
    print(arp_request_boradcast.summary())

    arp_request.show()
    broadcast.show()
    arp_request_boradcast.show()

    # show all feilds & informations
    scapy.ls(scapy.Ether())


scan(("192.168.57.1"))
