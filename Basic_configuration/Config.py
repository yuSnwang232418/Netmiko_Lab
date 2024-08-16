from netmiko import ConnectHandler
from Input_command import get_command
from Input_Device_list import get_device
from Connect import connect_to_device
from Use_thread import create_thread

import sys
import threading


def test_to_connect():
    for i in range(len(device_list)):
        connect_to_device(device_list[i], commands)


if __name__ == '__main__':
    # Read the commands from file
    commands = get_command()
    # print(commands)
    # Read the device list
    device_list = get_device(sys.argv[2])
    # test_to_connect()
    create_thread(device_list, commands)
    # print(device_list)
