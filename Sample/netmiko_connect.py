# from netmiko import Netmiko
#
# connection = Netmiko(host='192.168.217.5', port='22', username='wyx', password='wyx', device_type='cisco_ios')
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.217.5',
    'username': 'wyx',
    'password': 'wyx',
    'port': 22,
    'secret': ''  # enable password
    'verbose' 'true'
}
connection = ConnectHandler(**cisco_device)
# prompt = connection.find_prompt()
# # print(prompt)
# if '>' in prompt:
#     connection.enable()
#
# output = connection.send_command('sh ip int brief')
# print(output)
#
# if not connection.check_config_mode():
#     connection.config_mode()
# connection.exit_config_mode()

print('Entering the enable mode')
connection.enable()

commands = ['int lo0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username wyx1 password wyx']
# cmd = 'ip ssh version 2; access-list 1 permit any'
# connection.send_config_set(cmd.split(';'))
connection.send_config_set(commands) # auto enter conf t and exit to enable mode
# configure form file
# connection.send_config_from_file('ospf.txt')

connection.send_command('wr')


print('close connection')
connection.disconnect()
