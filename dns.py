#!/usr/bin/env python3
import socket
import sys

try:
    arg = sys.argv[1]
    domain = sys.argv[1]
except IndexError:
    print('Error: You need to supply a domain name.')
    print('Correct usage is:', sys.argv[0], 'cloudabove.com')

    domain = input('Domain Name: ')

print('-------------------------------------')

print('\tDNS Report: \n\n',
'Domain Name:\t', domain,
'\nA Record:\t', socket.gethostbyname(domain),
'\nMX Record:\t', 'mx.example.com',
sep='')

print('-------------------------------------')
