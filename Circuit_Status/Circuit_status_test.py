from Read_circuit_list import read_circuit_list
from Input_Device_list import get_device
from connect_and_test import connect_and_test
from Use_thread import create_thread

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please enter as following: Circuit_status_test.py Circuit_list.txt device_list.txt")
    device_list = get_device(sys.argv[2])
    ping_command_dict = read_circuit_list()
    # print(ping_command_dict)
    # connect_and_test(ping_command_dict.items(), device_list)
    create_thread(ping_command_dict, device_list)
