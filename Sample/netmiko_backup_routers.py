from netmiko import ConnectHandler
from datetime import datetime

with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:

    cisco_device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'wyx',
           'password': 'wyx',
           'port': 22,             # optional, default 22
           'secret': '',      # this is the enable password
           'verbose': True         # optional, default False
           }
    connection = ConnectHandler(**cisco_device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')

    # creating the backup filename (hostname_date_backup.txt)
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    # print(hostname)

    # getting the current date (year-month-day)
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{hostname}_{year}-{month}-{day}.txt'

    # writing the backup to the file
    with open(filename, 'w') as f1:
        f1.write(output)

    print('Closing connection')
    connection.disconnect()
