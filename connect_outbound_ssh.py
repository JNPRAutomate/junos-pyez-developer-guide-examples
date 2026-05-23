"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Connect to Junos Devices Using Junos PyEZ > Connect to a Device Using Outbound SSH
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-connection-methods.html
"""

import socket
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from getpass import getpass
from pprint import pprint


"""
  Listen on TCP port 2200 for incoming SSH session with a Junos device.
  Upon connecting, collect and print the devices facts,
  then disconnect from that device and wait for more connections.
"""


def launch_junos_proxy(client, addr):
    val = {
            'MSG-ID': None,
            'MSG-VER': None,
            'DEVICE-ID': None,
            'HOST-KEY': None,
            'HMAC': None
            }

    msg = ''
    count = 0

    while count < 5:
        c = client.recv(1)
        c = c.decode("utf-8")
        msg += str(c)
        if c == '\n':
            count += 1

    for line in msg.splitlines():
        (key, value) = line.split(': ')
        val[key] = value
        print("{}: {}".format(key, val[key]))

    return client.fileno()


def main():

    PORT = 2200

    junos_username = input('Junos OS username: ')
    junos_password = getpass('Junos OS password: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('', PORT))
    s.listen(5)
    print('\nListening on port %d for incoming sessions ...' % (PORT))

    sock_fd = 0
    while True:
        client, addr = s.accept()
        print('\nGot a connection from %s:%d' % (addr[0], addr[1]))
        sock_fd = launch_junos_proxy(client, addr)

        print('Logging in ...')
        try:
            with Device(host=None, sock_fd=sock_fd, user=junos_username, passwd=junos_password) as dev:
                pprint(dev.facts)
        except ConnectError as err:
            print ("Cannot connect to device: {0}".format(err))

if __name__ == "__main__":
    main()
