import netmiko
from Read_from_TXT import read_from_txt
from Read_from_JSON import read_from_json
from Get_Username import get_input
from Get_Password_hide import get_credential

##########################################################################
# 1. Read from TXT
# my_device_list = read_from_txt()
##########################################################################
# 2. Read from JSON
my_device_list = read_from_json()

num = len(my_device_list)
# num = 1
for i in range(num):
    # If no username, enter it
    if 'username' not in my_device_list[i]:
        username = get_input('Enter username: ')
        my_device_list[i]['username'] = username
    # If no password, enter it, can't see
    if 'password' not in my_device_list[i]:
        password = get_credential('Enter password: ')
        my_device_list[i]['password'] = password
    try:
        connection = netmiko.ConnectHandler(**my_device_list[i])
        print(connection.send_command('show int des'))
        print(connection.send_command('show clock'))
        connection.disconnect()
    # Authentication issue
    except netmiko.NetmikoAuthenticationException:
        print(f'Warn: Authentication failed to: {my_device_list[i]["host"]}')
    # Timeout issue
    except netmiko.NetmikoTimeoutException as e:
        print(f'Warn: Device {my_device_list[i]["host"]} might down', e)
