def read_from_txt():
    my_device_list = []
    # Read from TXT file
    with (open('device_list.txt', 'r') as f):
        devices = f.readlines()
        for device in devices:
            if device == '\n':
                continue
            else:
                if device.endswith('\n'):
                    cur_device = device[:-1].split(':')
                else:
                    cur_device = device.split(':')
                # print(cur_device)
                cur_device_info = {
                    'host': cur_device[0],
                    'port': cur_device[1],
                    'username': cur_device[2],
                    'password': cur_device[3],
                    'device_type': 'cisco_ios',
                    'secret': '',
                    'verbose': 'true'
                }
                my_device_list.append(cur_device_info)
        # print(my_device_list[0])
        return my_device_list
