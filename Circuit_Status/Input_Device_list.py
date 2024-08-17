from getpass import getpass


def get_device(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
        # print(content)

    devices_list = []
    for info in content:
        # Skip the empty line
        if info == '\n':
            continue
        else:
            cur_device = info[:-1].split(':')
            # print(cur_device)
            # Format the device information for Netmiko connection
            cur_device_info = {
                'host': cur_device[0],
                'port': cur_device[1],
                'username': cur_device[2],
                'password': cur_device[3],
                'device_type': 'cisco_ios',
                'secret': '',
                'verbose': 'true'
            }
            # If the username is not in the file, input manually
            if cur_device_info['username'] == '':
                cur_device_info['username'] = input(f"Please enter username for {cur_device_info['host']}\n")
            # if the password is not in the file, getpass
            if cur_device_info['password'] == '':
                cur_device_info['password'] = getpass(f"Please enter password for {cur_device_info['host']}\n")
            # Append all devices' information into a list
            devices_list.append(cur_device_info)
    return devices_list
