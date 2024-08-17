import threading
from connect_and_test import connect_and_test


def create_thread(ping_dict, device_list):
    # Create empty thread list
    my_thread = []
    for backbone_ID, ping_task in ping_dict.items():
        th = threading.Thread(target=connect_and_test, args=(backbone_ID, ping_task, device_list))
        my_thread.append(th)
    for th in my_thread:
        th.start()
    for th in my_thread:
        th.join()
