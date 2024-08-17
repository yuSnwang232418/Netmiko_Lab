import netmiko
from netmiko import ConnectHandler
import os
from datetime import datetime


def connect_backup(device):
    # get the current time
    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        print(f'Start to backup the current config for {device["host"]}')
        command_execution = connection.send_command("show run")
        # print(command_execution)
        # Save the configuration to file in the related dir.
        dir_name = connection.base_prompt + " Config Backup"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        file_name = f"{connection.base_prompt}_{year}-{month}-{day}-{hour}-{minute}.txt"
        file_path = '\\'.join((dir_name, file_name))
        with open(file_path,'w') as w:
            w.write(command_execution)
        connection.exit_enable_mode()
        connection.disconnect()
    except netmiko.NetmikoAuthenticationException:
        print(f"Warning: The username or password of the {device['host']} might be wrong")
    except netmiko.NetmikoTimeoutException:
        print(f"The device {device['host']} is unreachable. Please check it.")