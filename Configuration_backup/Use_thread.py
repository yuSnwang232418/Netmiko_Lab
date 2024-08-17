import threading
from Connect_and_backup import connect_backup


def create_thread(device_list):
    # Create empty thread list
    my_thread = []
    for cur_device in device_list:
        th = threading.Thread(target=connect_backup, args=(cur_device, ))
        my_thread.append(th)
    for th in my_thread:
        th.start()
    for th in my_thread:
        th.join()
