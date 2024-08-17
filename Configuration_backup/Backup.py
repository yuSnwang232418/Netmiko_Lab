from Input_device import get_device
from Use_thread import create_thread

if __name__ == "__main__":
    device_list = get_device()
    create_thread(device_list)
