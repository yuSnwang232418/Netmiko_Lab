import time
from netmiko import ConnectHandler
import threading
from datetime import datetime


def func(my_device):
    connection = ConnectHandler(**my_device)
    print(f"Connecting to {my_device['host']}")

    # Get the hostname of device
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    connection.enable()
    output = connection.send_config_from_file('command.txt')
    connection.exit_enable_mode()
    print(connection.find_prompt())

    # current time
    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
    file_name = f"{hostname}_{year}-{month}-{day}-{hour}-{minute}.txt"

    # save the output to file
    with open(file_name, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')

    # Stop the connection
    print(f"Disconnecting from {my_device['host']}")
    connection.disconnect()


if __name__ == '__main__':

    start = time.time()
    my_device_list = []
    threads = []
    with open('device_list.txt', 'r') as f:
        devices = f.read().splitlines()
        # print(devices)

    for device in devices:
        cur_device = device.split(':')
        cisco_device = {
            'device_type': 'cisco_ios',
            'host': cur_device[0],
            'username': cur_device[2],
            'password': cur_device[3],
            'port': cur_device[1],
            'secret': ''  # enable password
            'verbose' 'true'
        }
        my_device_list.append(cisco_device)
        th = threading.Thread(target=func, args=(cisco_device,))
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    end = time.time()
    print(f'Total execution time:{end - start}')
