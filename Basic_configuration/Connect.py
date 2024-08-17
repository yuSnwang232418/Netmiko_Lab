import netmiko
from netmiko import ConnectHandler

import time


def connect_to_device(cur_device, commands):
    try:
        connection = ConnectHandler(**cur_device)
        print(f"Connection to {connection.base_prompt} is established")
        connection.enable()
        for command in commands:
            connection.send_command(command, expect_string=r'#')
        # Confirm the current configuration
        print(connection.send_command('show run | s router ospf 1'))
        print('Waiting for OSPF neighbor to establish...60 seconds')
        time.sleep(60)
        print(connection.send_command('show ip ospf nei'))
        connection.exit_enable_mode()
        connection.disconnect()
    except netmiko.NetmikoAuthenticationException:
        print(f"Warning: The username or password of the {cur_device['host']} might be wrong")
    except netmiko.NetmikoTimeoutException:
        print(f"The device {cur_device['host']} is unreachable. Please check it.")


