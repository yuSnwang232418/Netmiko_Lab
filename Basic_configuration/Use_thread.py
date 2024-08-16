import threading
from Connect import connect_to_device


def create_thread(device_list, commands):
    # Create empty thread list
    my_thread = []
    for cur_device in device_list:
        th = threading.Thread(target=connect_to_device, args=(cur_device, commands))
        my_thread.append(th)
    for th in my_thread:
        th.start()
    for th in my_thread:
        th.join()
