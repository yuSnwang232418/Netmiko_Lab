import netmiko
from netmiko import ConnectHandler
from collections import defaultdict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def check_output(output):
    if "Success rate is 100 percent" in output:
        return True
    return False


def send_email(backbone_id):
    from_addr = 'yusnwang232@gmail.com'
    to_addr = 'yusnwang232@gmail.com'
    my_message = f"Backbone circuit {backbone_id} is down. Please check it now."
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Backbone Circuit Down Report'
    msg.attach(MIMEText(my_message, 'plain'))
    # Sending the email via Gmail's SMTP server on port 587
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
    server.starttls()

    # Logging in to Gmail and sending the e-mail
    server.login('yusnwang232', 'kmje pdpg owyr jxkn')
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


def connect_and_test(backbone_id, tasks, device_list):
    print(tasks)
    # print(device_list)
    flag = True
    for task in tasks:
        try:
            # print(device_list[int(task[0])-1])
            connection = ConnectHandler(**device_list[int(task[0])-1], )
            print(f"Connection to {connection.base_prompt} is established")
            connection.enable()

            print(f"Backbone: {backbone_id}, ping tset: ")
            ping_output = connection.send_command(task[1], expect_string=r'#', read_timeout=60)
            # Either one way ping fails will lead to False
            if not check_output(ping_output):
                print(f"Backbone: {backbone_id}, ping tset try again: ")
                ping_output = connection.send_command(task[1], expect_string=r'#', read_timeout=60)
                if not check_output(ping_output):
                    flag = False
            connection.exit_enable_mode()
            connection.disconnect()
        except netmiko.NetmikoAuthenticationException:
            print(f"Warning: The username or password of the {task[0]} might be wrong")
        except netmiko.NetmikoTimeoutException:
            print(f"The device {task[0]} is unreachable. Please check it.")
    if not flag:
        print(f"{backbone_id} is hard down, please check")
        send_email(backbone_id)
    else:
        print(f"{backbone_id} check passed.")
